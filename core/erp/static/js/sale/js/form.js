var tblReplacement;
var vents = {
    items: {
        'cli': '',
        'pay_method': '',
        'date_joined': '',
        'subtotal': 0.00,
        'iva': 0.00,
        'pay_method': '',
        'money': '',
        'total': 0.00,
        'replacement': []
    },

    add: function (item) {
        this.items.replacement.push(item);
        this.list();
    },
    calculate_invoice: function () {
        var subtotal = 0.00;
        var iva = $('input[name="iva"]').val();
        $.each(this.items.replacement, function (pos, dict) {
            dict.subtotal = dict.stock * parseFloat(dict.pvp);
            dict.pos = pos;
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;


        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.subtotal + this.items.iva;
        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));


        $('input[name="total"]').val(this.items.total.toFixed(2));
        $('input[name="ivacalc"]').val(this.items.iva.toFixed(2));
    },

    list: function () {
        this.calculate_invoice();
        tblReplacement = $('#tblReplacement').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,

            data: this.items.replacement,


            columns: [
                { "data": "id" },
                { "data": "name" },
                { "data": "code_replacement" },
                { "data": "pvp" },
                { "data": "cant" },
                { "data": "subtotal" }
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    }
                },



                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);

                    }
                },

                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '<input type="text", name="stock" class="form-control form-control-md" autocomplete="off" value="' + row.stock + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);

                    }
                }
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {
                $(row).find('input[name="stock"]').TouchSpin({
                    min: 1,
                    max: 100000,
                    step: 1
                });
            },
            initComplete: function (settings, json) {

            }
        });
    }
};

$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: "es",

    });


    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        maxDate: moment().format("YYYY-MM-DD"),
        minDate: moment().format("YYYY-MM-DD")
    });

    $("input[name='iva']").TouchSpin({
        min: 0.19,
        max: 0.19,
        step: 0.19,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    }).on('change', function () {
        vents.calculate_invoice();
    }).
        val(0.19);


    //search clients

    //search replacement
    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_replacement',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.stock = 1;
            ui.item.subtotal = 0.00;
            console.log(vents.items);
            vents.add(ui.item);
            $(this).val('');

        }
    });

    $('.btnRemoveAll').on('click', function () {
        if (vents.items.replacement.length === 0) {
            Swal.fire({
                icon: "error",
                title: "Listado Vacío",
                text: "Debe completar el listado",
            });
            return false
        };
        alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?', function () {
            vents.items.replacement = [];
            vents.list();
        });
    });

    // event stock
    $('#tblReplacement tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblReplacement.cell($(this).closest('td, li')).index();
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?', function () {
                vents.items.replacement.splice(tr.row, 1);
                vents.list();
            });
        })
        .on('change', 'input[name="stock"]', function () {
            console.clear();
            var stock = parseInt($(this).val());
            var tr = tblReplacement.cell($(this).closest('td, li')).index();
            vents.items.replacement[tr.row].stock = stock;
            vents.calculate_invoice();
            $('td:eq(5)', tblReplacement.row(tr.row).node()).html('$' + vents.items.replacement[tr.row].subtotal.toFixed(2));
        });


    $('.btnClearSearch').on('click', function () {
        $('input[name="search"]').val('').focus();
    });

    //event submit
    $('form').on('submit', function (e) {
        e.preventDefault();

        if (vents.items.replacement.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        vents.items.date_joined = $('input[name="date_joined"]').val();
        vents.items.cli = $('select[name="cli"]').val();
        vents.items.pay_method = $('select[name="pay_method"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/erp/dashboard/';
        });
    });

    vents.list();
});
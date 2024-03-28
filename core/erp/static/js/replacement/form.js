/*calculate_invoice: function () {
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
};
$(function () {
    $("input[name='iva']").TouchSpin({
        min: 1.4,
        max: 1.4,
        step: 1.4,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    }).val(1.4);
});*/
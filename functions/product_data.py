def variant_id(color, size):
    product_data = {
    "S":
        {
            "berry":4041,
            "black heather":8923,
            "white":4011,
            "black":4016,
            "grey":8460,
            "gold":4081,
            "orange":8516,
            "red":4141,
            "navy":4111,
            "royal":8530,
            "teal":8481,
            "green":4086,
            "citron":14659
        },
    "M":
        {
            "berry":4042,
            "black heather":8924,
            "white":4012,
            "black": 4017,
            "grey":8461,
            "gold":4082,
            "orange":8517,
            "red":4142,
            "navy":4112,
            "royal":8531,
            "teal":8482,
            "green":4087,
            "citron":14660
        },
    "L":
        {
            "berry":4043,
            "black heather":8925,
            "white":4013,
            "black": 4018,
            "grey":8462,
            "gold":4083,
            "orange":8518,
            "red":4143,
            "navy":4113,
            "royal":8532,
            "teal":8483,
            "green":4088,
            "citron":14661
        },
    "XL":
        {
            "berry":4044,
            "black heather":8926,
            "white":4014,
            "black": 4019,
            "grey":8463,
            "gold":4084,
            "orange":8519,
            "red":4144,
            "navy":4114,
            "royal":8533,
            "teal":8484,
            "green":4089,
            "citron":14662
        }
    }   
    return product_data[size][color]
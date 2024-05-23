import json
import re
import scrapy

data=[
{
    'id': 0,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'MARQUISE',
            ],
            [
                'default_code',
                '=',
                'MARQUISE',
            ],
            [
                'barcode',
                '=',
                'MARQUISE',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' PERSEIDAS',
            ],
            [
                'default_code',
                '=',
                ' PERSEIDAS',
            ],
            [
                'barcode',
                '=',
                ' PERSEIDAS',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' ESPIGA',
            ],
            [
                'default_code',
                '=',
                ' ESPIGA',
            ],
            [
                'barcode',
                '=',
                ' ESPIGA',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 1,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'LADY RODIO ZAFIRO',
            ],
            [
                'default_code',
                '=',
                'LADY RODIO ZAFIRO',
            ],
            [
                'barcode',
                '=',
                'LADY RODIO ZAFIRO',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY RODIO RUBÍ',
            ],
            [
                'default_code',
                '=',
                ' LADY RODIO RUBÍ',
            ],
            [
                'barcode',
                '=',
                ' LADY RODIO RUBÍ',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY RODIO ESMERALDA',
            ],
            [
                'default_code',
                '=',
                ' LADY RODIO ESMERALDA',
            ],
            [
                'barcode',
                '=',
                ' LADY RODIO ESMERALDA',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 2,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'LADY RODIO TSA',
            ],
            [
                'default_code',
                '=',
                'LADY RODIO TSA',
            ],
            [
                'barcode',
                '=',
                'LADY RODIO TSA',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY RODIO TOPACIO LONDON',
            ],
            [
                'default_code',
                '=',
                ' LADY RODIO TOPACIO LONDON',
            ],
            [
                'barcode',
                '=',
                ' LADY RODIO TOPACIO LONDON',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY RODIO AGUA',
            ],
            [
                'default_code',
                '=',
                ' LADY RODIO AGUA',
            ],
            [
                'barcode',
                '=',
                ' LADY RODIO AGUA',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY RODIO AMA',
            ],
            [
                'default_code',
                '=',
                ' LADY RODIO AMA',
            ],
            [
                'barcode',
                '=',
                ' LADY RODIO AMA',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 3,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'serenity tu y yo two diamante',
            ],
            [
                'default_code',
                '=',
                'serenity tu y yo two diamante',
            ],
            [
                'barcode',
                '=',
                'serenity tu y yo two diamante',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' esmeralda 2 brillantes',
            ],
            [
                'default_code',
                '=',
                ' esmeralda 2 brillantes',
            ],
            [
                'barcode',
                '=',
                ' esmeralda 2 brillantes',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' bridge five de brillantes y solitario esmer',
            ],
            [
                'default_code',
                '=',
                ' bridge five de brillantes y solitario esmer',
            ],
            [
                'barcode',
                '=',
                ' bridge five de brillantes y solitario esmer',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' symmetry five',
            ],
            [
                'default_code',
                '=',
                ' symmetry five',
            ],
            [
                'barcode',
                '=',
                ' symmetry five',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': False,
        },
    },
},
{
    'id': 4,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'serenity esmeralda octo',
            ],
            [
                'default_code',
                '=',
                'serenity esmeralda octo',
            ],
            [
                'barcode',
                '=',
                'serenity esmeralda octo',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' lady esmeralda brasil oval',
            ],
            [
                'default_code',
                '=',
                ' lady esmeralda brasil oval',
            ],
            [
                'barcode',
                '=',
                ' lady esmeralda brasil oval',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': False,
        },
    },
},{
    'id': 5,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'forever rubí',
            ],
            [
                'default_code',
                '=',
                'forever rubí',
            ],
            [
                'barcode',
                '=',
                'forever rubí',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' brillantes y RUBÍ',
            ],
            [
                'default_code',
                '=',
                ' brillantes y RUBÍ',
            ],
            [
                'barcode',
                '=',
                ' brillantes y RUBÍ',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' TURMALINA ROSA',
            ],
            [
                'default_code',
                '=',
                ' TURMALINA ROSA',
            ],
            [
                'barcode',
                '=',
                ' TURMALINA ROSA',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 6,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'venus topacio london',
            ],
            [
                'default_code',
                '=',
                'venus topacio london',
            ],
            [
                'barcode',
                '=',
                'venus topacio london',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' asymmetry topacio sky',
            ],
            [
                'default_code',
                '=',
                ' asymmetry topacio sky',
            ],
            [
                'barcode',
                '=',
                ' asymmetry topacio sky',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' bridge five de brillantes y topacio london',
            ],
            [
                'default_code',
                '=',
                ' bridge five de brillantes y topacio london',
            ],
            [
                'barcode',
                '=',
                ' bridge five de brillantes y topacio london',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': False,
        },
    },
},
 {
    'id': 7,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'baguettes y topacio',
            ],
            [
                'default_code',
                '=',
                'baguettes y topacio',
            ],
            [
                'barcode',
                '=',
                'baguettes y topacio',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' lady topacio london',
            ],
            [
                'default_code',
                '=',
                ' lady topacio london',
            ],
            [
                'barcode',
                '=',
                ' lady topacio london',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': False,
        },
    },
},
{
    'id': 8,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'serenity topacio london blue oval',
            ],
            [
                'default_code',
                '=',
                'serenity topacio london blue oval',
            ],
            [
                'barcode',
                '=',
                'serenity topacio london blue oval',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' trilogy topacios sky',
            ],
            [
                'default_code',
                '=',
                ' trilogy topacios sky',
            ],
            [
                'barcode',
                '=',
                ' trilogy topacios sky',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' trilogy topacio sky y london',
            ],
            [
                'default_code',
                '=',
                ' trilogy topacio sky y london',
            ],
            [
                'barcode',
                '=',
                ' trilogy topacio sky y london',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' ENMA',
            ],
            [
                'default_code',
                '=',
                ' ENMA',
            ],
            [
                'barcode',
                '=',
                ' ENMA',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': False,
        },
    },
},
{
    'id': 9,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'SERENITY AGUAMARINA OVAL',
            ],
            [
                'default_code',
                '=',
                'SERENITY AGUAMARINA OVAL',
            ],
            [
                'barcode',
                '=',
                'SERENITY AGUAMARINA OVAL',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' SERENITY CIANITA OVAL',
            ],
            [
                'default_code',
                '=',
                ' SERENITY CIANITA OVAL',
            ],
            [
                'barcode',
                '=',
                ' SERENITY CIANITA OVAL',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' BAGUETTES Y ZAFIRO AZUL',
            ],
            [
                'default_code',
                '=',
                ' BAGUETTES Y ZAFIRO AZUL',
            ],
            [
                'barcode',
                '=',
                ' BAGUETTES Y ZAFIRO AZUL',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
 {
    'id': 10,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'LADY TOPACIO ROSA',
            ],
            [
                'default_code',
                '=',
                'LADY TOPACIO ROSA',
            ],
            [
                'barcode',
                '=',
                'LADY TOPACIO ROSA',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY TWIN',
            ],
            [
                'default_code',
                '=',
                ' LADY TWIN',
            ],
            [
                'barcode',
                '=',
                ' LADY TWIN',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY XL',
            ],
            [
                'default_code',
                '=',
                ' LADY XL',
            ],
            [
                'barcode',
                '=',
                ' LADY XL',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY SOLITARIO',
            ],
            [
                'default_code',
                '=',
                ' LADY SOLITARIO',
            ],
            [
                'barcode',
                '=',
                ' LADY SOLITARIO',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 11,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'LADY ZAFIRO NARANJA OCTO',
            ],
            [
                'default_code',
                '=',
                'LADY ZAFIRO NARANJA OCTO',
            ],
            [
                'barcode',
                '=',
                'LADY ZAFIRO NARANJA OCTO',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY ZAFIRO NARANJA OVAL',
            ],
            [
                'default_code',
                '=',
                ' LADY ZAFIRO NARANJA OVAL',
            ],
            [
                'barcode',
                '=',
                ' LADY ZAFIRO NARANJA OVAL',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY ESMERALDA OVAL',
            ],
            [
                'default_code',
                '=',
                ' LADY ESMERALDA OVAL',
            ],
            [
                'barcode',
                '=',
                ' LADY ESMERALDA OVAL',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' LADY TURMALINA VERDE',
            ],
            [
                'default_code',
                '=',
                ' LADY TURMALINA VERDE',
            ],
            [
                'barcode',
                '=',
                ' LADY TURMALINA VERDE',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 12,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'gallery alianza completa',
            ],
            [
                'default_code',
                '=',
                'gallery alianza completa',
            ],
            [
                'barcode',
                '=',
                'gallery alianza completa',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' gallery media alianza 10 bague',
            ],
            [
                'default_code',
                '=',
                ' gallery media alianza 10 bague',
            ],
            [
                'barcode',
                '=',
                ' gallery media alianza 10 bague',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' gallery media alianza 7',
            ],
            [
                'default_code',
                '=',
                ' gallery media alianza 7',
            ],
            [
                'barcode',
                '=',
                ' gallery media alianza 7',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' gallery doble media',
            ],
            [
                'default_code',
                '=',
                ' gallery doble media',
            ],
            [
                'barcode',
                '=',
                ' gallery doble media',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 13,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'gallery media alianza 11',
            ],
            [
                'default_code',
                '=',
                'gallery media alianza 11',
            ],
            [
                'barcode',
                '=',
                'gallery media alianza 11',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' gallery media alianza 21',
            ],
            [
                'default_code',
                '=',
                ' gallery media alianza 21',
            ],
            [
                'barcode',
                '=',
                ' gallery media alianza 21',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' gallery media alianza 9',
            ],
            [
                'default_code',
                '=',
                ' gallery media alianza 9',
            ],
            [
                'barcode',
                '=',
                ' gallery media alianza 9',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 14,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'paredilla',
            ],
            [
                'default_code',
                '=',
                'paredilla',
            ],
            [
                'barcode',
                '=',
                'paredilla',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' riviere doble media alianza',
            ],
            [
                'default_code',
                '=',
                ' riviere doble media alianza',
            ],
            [
                'barcode',
                '=',
                ' riviere doble media alianza',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 15,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'riviere media alianza 13',
            ],
            [
                'default_code',
                '=',
                'riviere media alianza 13',
            ],
            [
                'barcode',
                '=',
                'riviere media alianza 13',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' riviere media alianza 9',
            ],
            [
                'default_code',
                '=',
                ' riviere media alianza 9',
            ],
            [
                'barcode',
                '=',
                ' riviere media alianza 9',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' riviere media alianza 11 brillantes ob',
            ],
            [
                'default_code',
                '=',
                ' riviere media alianza 11 brillantes ob',
            ],
            [
                'barcode',
                '=',
                ' riviere media alianza 11 brillantes ob',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 16,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                'ETERNITY',
            ],
            [
                'default_code',
                '=',
                'ETERNITY',
            ],
            [
                'barcode',
                '=',
                'ETERNITY',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 17,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'TRILOGY AMATISTA',
            ],
            [
                'default_code',
                '=',
                'TRILOGY AMATISTA',
            ],
            [
                'barcode',
                '=',
                'TRILOGY AMATISTA',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' TRILOGY TOPACIO SKY RECT',
            ],
            [
                'default_code',
                '=',
                ' TRILOGY TOPACIO SKY RECT',
            ],
            [
                'barcode',
                '=',
                ' TRILOGY TOPACIO SKY RECT',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
},
{
    'id': 18,
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'filter_id': 1,
        'template_key': 'website_sale.dynamic_filter_template_product_product_borderless_1',
        'limit': 16,
        'search_domain': [
            [
                'public_categ_ids',
                'child_of',
                17,
            ],
            '|',
            '|',
            '|',
            [
                'name',
                'ilike',
                'SINGULAR',
            ],
            [
                'default_code',
                '=',
                'SINGULAR',
            ],
            [
                'barcode',
                '=',
                'SINGULAR',
            ],
            '|',
            '|',
            [
                'name',
                'ilike',
                ' vila',
            ],
            [
                'default_code',
                '=',
                ' vila',
            ],
            [
                'barcode',
                '=',
                ' vila',
            ],
        ],
        'with_sample': False,
        'context': {
            '_bugfix_force_minimum_max_limit_to_16': True,
        },
    },
}





]
class MyspiderSpider(scrapy.Spider):
    name = "myspider"

    def start_requests(self):
        for item in data:
            url = 'https://www.abrines.es/website/snippet/filters'
            headers = {
                'authority': 'www.abrines.es',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.abrines.es',
                'referer': 'https://www.abrines.es/altajoyeria/anillos',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            }
            yield scrapy.Request(
                        url,
                        method='POST',
                        headers=headers,
                        body=json.dumps(item),
                        callback=self.parse,
                        dont_filter=True,

                    )

    def parse(self, response):
        json_data = json.loads(response.text)
        # print(json_data['result'])
        if "result" in json_data:
            for data in json_data["result"]:

                a_tag_match = re.search(r'<a\s+[^>]*>(.*?)</a>', data, re.DOTALL)
                product_id_match = re.search(r'<input\s+[^>]*data-product-id="([^"]+)"[^>]*>', data, re.DOTALL)
                product_id = product_id_match.group(1) if product_id_match else None

                # print(data)
                print(product_id)
                a_tag = a_tag_match.group(0) if a_tag_match else None
                if a_tag:
                    href_match = re.search(r'href="([^"]+)"', a_tag)
                    href = href_match.group(1) if href_match else None

                    # print(href)
                    url="https://www.abrines.es/shop/110persbrwg-anillo-perseidas-brillantes-ob-{}#attr=".format(product_id)
                    if product_id:
                        yield scrapy.Request(
                            url=url,
                            callback=self.details,
                        )

    def details(self, response):
        url = response.url
        # input()
        product_title = response.xpath('//*[@id="product_details"]/h1/text()').get()
        product_paragraph = response.xpath('//*[@id="product_details"]/p/text()').get()
        displayed_price = response.xpath('//span[@class="oe_currency_value"]/text()').get()
        image_src = response.xpath('//div[@class="d-flex align-items-center justify-content-center h-100 oe_unmovable"]/img/@src').get()

        data = {
            'Product Title': product_title,
            'Product Details Paragraph': product_paragraph,
            'Displayed Price': displayed_price,
            'Image Source': "https://www.abrines.es{}".format(image_src) if image_src else None,
            'Detail Page Url': url
        }
        yield data

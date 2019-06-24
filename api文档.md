创建订单

请求协议|请求方法：HTTP|POST

接口路径：v1/order/<:rid>

接口使用状态：正常启用

请求头部：

| 头部标签 | 必填  | 头部内容 | 
| :------------ | :------------ |

鉴权：

验证类型：
无

请求参数
参数类型：Json
根类型: Object

  参数名            	说明  	必填  	类型      	值可能性	限制  	示例  
  uid            	    	是   	[number]	    	1   	    
  total_price    	    	是   	[number]	    	37  	    
  note           	    	是   	[string]	    	请快一点	    
  rid            	    	是   	[number]	    	1   	    
  coupon_discount	    	是   	[number]	    	2   	    
  lists          	    	是   	[array] 	    	    	    
  lists>>did     	    	是   	[number]	    	1   	    
  lists>>quantity	    	是   	[number]	    	2   	    

成功示例[Mock API]：

mock api：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=v1/order/<:rid>

    {
        "error_code": 0,
        "msg": "ok",
        "request": "POST /v1/order/1"
    }

失败示例[Mock API]：

mock api：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=v1/order/<:rid>&resultType=failure

    

详细说明：

    ##发表评论
    
    **请求协议|请求方法**：HTTP|POST
    
    **接口路径**：v1/comment/<:rid>
    
    **接口使用状态**：正常启用
    
    **请求头部**：
    
    | 头部标签 | 必填  | 头部内容 | 
    | :------------ | :------------ |
    
    **鉴权**：
    
    **验证类型**：
    无
    
    **REST参数**：
    
    | 参数名  | 说明 | 必填 | 类型 | 值可能性 | 限制 | 示例 |
    | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
    |uid||是|[number]|:||1|
    |content||是|[string]|:||难吃|
    
    **返回参数**
    参数类型：Json
    根类型: Object
    
    | 参数名  | 说明 |  | 类型 | 值可能性 | 限制 | 示例 |
    | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
    |error_code||是|[number]|:||0|
    |msg||是|[string]|:||ok|
    |request||是|[string]|:||POST /v1/comment/1|
    
    **成功示例[Mock API]**：
    
    
    **mock api**：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=v1/comment/<:rid>

{
    "error_code": 0,
    "msg": "ok",
    "request": "POST /v1/comment/1"
}

    **失败示例[Mock API]**：
    
    
    **mock api**：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=v1/comment/<:rid>&resultType=failure

    **详细说明**：
    
    

获得餐厅菜单种类

请求协议|请求方法：HTTP|GET

接口路径：/v1/category/<:rid>

接口使用状态：正常启用

请求头部：

| 头部标签 | 必填  | 头部内容 | 
| :------------ | :------------ |

鉴权：

验证类型：
无

返回参数
参数类型：Json
根类型: Object

  参数名             	说明  	    	类型      	值可能性	限制  	示例                 
  category        	    	是   	[array] 	    	    	                   
  category>>name  	    	是   	[string]	:   	    	zibinzheng@yeah.net
  category>>weight	    	是   	[number]	:   	    	1                  
  number          	    	是   	[number]	:   	    	3                  

成功示例[Mock API]：

mock api：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/category/<:rid>

    {
        "category": [
            {
                "name": "zibinzheng@yeah.net",
                "weight": 1
            },
            {
                "name": "甜品小食",
                "weight": 1
            },
            {
                "name": "招牌简餐",
                "weight": 1
            }
        ],
        "number": 3
    }

失败示例[Mock API]：

mock api：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/category/<:rid>&resultType=failure

    

详细说明：

    ##获取菜单列表
    
    **请求协议|请求方法**：HTTP|GET
    
    **接口路径**：/v1/dish/<:rid>
    
    **接口使用状态**：正常启用
    
    **请求头部**：
    
    | 头部标签 | 必填  | 头部内容 | 
    | :------------ | :------------ |
    
    **鉴权**：
    
    **验证类型**：
    无
    
    **返回参数**
    参数类型：Json
    根类型: Object
    
    | 参数名  | 说明 |  | 类型 | 值可能性 | 限制 | 示例 |
    | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
    |dishes||是|[array]||||
    |dishes>>category||是|[string]|:||甜品小食|
    |dishes>>id||是|[number]|:||1|
    |dishes>>image||是|[string]|:||static/upload/20190622/e0dd4021576a42668d4a63e3f140745a.jpg|
    |dishes>>name||是|[string]|:||雪花酥|
    |dishes>>price||是|[number]|:||10|
    |number||是|[number]|:||3|
    
    **成功示例[Mock API]**：
    
    
    **mock api**：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/dish/<:rid>

{
    "dishes": [
        {
            "category": "甜品小食",
            "id": 1,
            "image": "static/upload/20190622/e0dd4021576a42668d4a63e3f140745a.jpg",
            "name": "雪花酥",
            "price": 10
        },
        {
            "category": "甜品小食",
            "id": 2,
            "image": "static/upload/20190622/ae702e1a12c84079bbf35823d23e93aa.jpg",
            "name": "芒果Nicecream",
            "price": 8
        },
        {
            "category": "招牌简餐",
            "id": 3,
            "image": "static/upload/20190622/50ac2a04fc1647f282e4867a65b428b3.jpg",
            "name": "茶香排骨",
            "price": 30
        }
    ],
    "number": 3
}

    **失败示例[Mock API]**：
    
    
    **mock api**：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/dish/<:rid>&resultType=failure
    

{
   "msg": "No this restaurant"
}

    **详细说明**：
    
    
    

获取菜品详细信息

请求协议|请求方法：HTTP|GET

接口路径：/v1/dish/:rid/<:did

接口使用状态：正常启用

请求头部：

| 头部标签 | 必填  | 头部内容 | 
| :------------ | :------------ |

鉴权：

验证类型：
无

返回参数
参数类型：Json
根类型: Object

  参数名     	说明  	    	类型      	值可能性	限制  	示例                                      
  category	    	是   	[string]	:   	    	甜品小食                                    
  id      	    	是   	[number]	:   	    	1                                       
  image   	    	是   	[string]	:   	    	static/upload/20190622/e0dd4021576a42668d4a63e3f140745a.jpg
  name    	    	是   	[string]	:   	    	雪花酥                                     
  price   	    	是   	[number]	:   	    	10                                      
  summary 	    	是   	[string]	:   	    	<p>南京特产，喵喵喵</p>                         

成功示例[Mock API]：

mock api：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/dish/:rid/<:did

    {
        "category": "甜品小食",
        "id": 1,
        "image": "static/upload/20190622/e0dd4021576a42668d4a63e3f140745a.jpg",
        "name": "雪花酥",
        "price": 10,
        "summary": "<p>南京特产，喵喵喵</p>"
    }
    

失败示例[Mock API]：

mock api：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/dish/:rid/<:did&resultType=failure

    

详细说明：

    ##获取餐厅评论
    
    **请求协议|请求方法**：HTTP|GET
    
    **接口路径**：/v1/comment/<:rid>
    
    **接口使用状态**：正常启用
    
    **请求头部**：
    
    | 头部标签 | 必填  | 头部内容 | 
    | :------------ | :------------ |
    
    **鉴权**：
    
    **验证类型**：
    无
    
    **返回参数**
    参数类型：Json
    根类型: Object
    
    | 参数名  | 说明 |  | 类型 | 值可能性 | 限制 | 示例 |
    | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
    |comments||是|[array]||||
    |comments>>content||是|[string]|:||难吃|
    |comments>>user||是|[string]|:||123|
    |number||是|[number]|:||1|
    
    **成功示例[Mock API]**：
    
    
    **mock api**：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/comment/<:rid>
    

{
    "comments": [
        {
            "content": "难吃",
            "user": "123"
        }
    ],
    "number": 1
}

    **失败示例[Mock API]**：
    
    
    **mock api**：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/comment/<:rid>&resultType=failure
    

    **详细说明**：
    
    
    

获取餐厅信息

请求协议|请求方法：HTTP|GET

接口路径：/v1/restaurant/1

接口使用状态：正常启用

请求头部：

| 头部标签 | 必填  | 头部内容 | 
| :------------ | :------------ |

鉴权：

验证类型：
无

返回参数
参数类型：Json
根类型: Object

  参数名    	说明  	    	类型      	值可能性	限制  	示例  
  name   	    	是   	[string]	:   	    	GOGO
  summary	    	是   	[null]  	    	    	    

成功示例[Mock API]：

mock api：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/restaurant/1

    {
        "name": "GOGO",
        "summary": null
    }
    

失败示例[Mock API]：

mock api：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/restaurant/1&resultType=failure

    

详细说明：

    ##获取用户优惠券
    
    **请求协议|请求方法**：HTTP|GET
    
    **接口路径**：/v1/coupon/<:rid>/<:uid>
    
    **接口使用状态**：正常启用
    
    **请求头部**：
    
    | 头部标签 | 必填  | 头部内容 | 
    | :------------ | :------------ |
    
    **鉴权**：
    
    **验证类型**：
    无
    
    **返回参数**
    参数类型：Json
    根类型: Object
    
    | 参数名  | 说明 |  | 类型 | 值可能性 | 限制 | 示例 |
    | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
    |coupons||是|[array]||||
    |coupons>>discount||是|[number]|:||1|
    |coupons>>expiration_date||是|[string]|:||2019-07-22T23:26:43.818776|
    |number||是|[number]|:||4|
    
    **成功示例[Mock API]**：
    
    
    **mock api**：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/coupon/<:rid>/<:uid>
    

{
    "coupons": [
        {
            "discount": 1,
            "expiration_date": "2019-07-22T23:26:43.818776"
        },
        {
            "discount": 3,
            "expiration_date": "2019-07-22T23:26:44.976556"
        },
        {
            "discount": 1,
            "expiration_date": "2019-07-22T23:28:40.848984"
        },
        {
            "discount": 1,
            "expiration_date": "2019-07-22T23:28:41.850987"
        }
    ],
    "number": 4
}

    **失败示例[Mock API]**：
    
    
    **mock api**：https://result.eolinker.com5BlM4Bv6a01f7756026aafe504b18ec66984a84f6d9a981?uri=/v1/coupon/<:rid>/<:uid>&resultType=failure
    

    **详细说明**：
    
    
    

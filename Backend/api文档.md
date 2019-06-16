注：经讨论，后台不能通过微信小程序获得用户身份，故传的api中部分需要用户id。目前假设唯一用户id是1，唯一餐厅id是1
中文采用unicode编码


get： url/v1/coupon/<uid>:（某个用户的coupon列表）

{

“discount”：float

“expiration_date”：string

}

get：url/v1/comment/<rid>:(某餐厅的评论列表)

{

“comments”：[{

```
 "content": string
 "user": string
```

}

]

"number": int

}

post: url/v1/comment/<rid>:(提交某餐厅评论)

{

“content”：string

“uid”：int（用户的id）

}

get：url/v1/comment/<rid>:(某餐厅菜单列表)

{

“dishes”：[{

```
 "id": int
 "name": string
 "image":url
 "price": float
 “category”:string
```

}

]

"number": int

}

get：url/v1/comment/<rid>/<did>:(某餐厅某菜品详细信息)

{

```
 "id": int
 "name": string
 "image":url
 "price": float
 “category”:string
 “summary”:string
```

}

get：url/v1/category/<rid>:(某餐厅菜品分类信息)

{

```
“categories”：[{

     "id": int
     "name": string
     "weight":int （根据权重确定摆放先后次序）
}

]

"number": int

```

}

post: url/v1/order/<rid> (提交订单)

{

“uid”：int

"total_price":float

"coupon_discount":float

"note":string

“carts”：[{

```
 "did": int
 "quantity": int
```

}

}


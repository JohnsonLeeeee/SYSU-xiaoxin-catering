base数据表（所有数据表的父类）：
状态（删除或未删除） 修改时间，创建时间
\
user数据表：
uid（主键） username phone number email sex avatar password（加密后的） confirm(是否验证邮箱)
\
管理员数据表（继承user，表示餐厅管理员）：
rid（外键，与restaurant数据表连接）
\
Address数据表：
id（主键），uid（外键，表示user），province_id,province_str,city_id,city_str,area_id,area_str,address(具体的街道)，is_default（是否为默认地址）
\
cart数据表：
id(主键)，uid（外键，表示user），did（外键，表示dish），quantity（表示数量）
\
dish数据表：
id（主键），rid（外键，表示restaurant）,name,price,summary.stock,tag,main_image
\
order数据表（订单):
id,order_sn（订单流水号）,uid（外键，用户）,cid（外键，优惠券）,total_price（菜单价格）,fair_price（运费价格）,pay_price（支付价格）,pay_sn（支付流水号）,prepay_id（预支付id）,note（备注）,express_status（送货状态）,comment_status（评价状态）,aid（外键，送货地址）,pay_time（支付时间）
\
coupon数据表：
id（主键），uid（外键，用户）,discount（优惠价格）,expiration_date（过期时间）
\
comment数据表：
id（主键），oid外键，订单），score（评分），content（评价内容）
\
restaurant数据表：
id(主键)，aid（外键，表示address），name,summary,main_image,month_count,total_count,view_count,comment_count


微信身份信息
JSONObject userInfoJSON = new JSONObject(result);
				Map userInfo = new HashMap();
				userInfo.put("openId", userInfoJSON.get("openId"));
				userInfo.put("nickName", userInfoJSON.get("nickName"));
				userInfo.put("gender", userInfoJSON.get("gender"));
				userInfo.put("city", userInfoJSON.get("city"));
				userInfo.put("province", userInfoJSON.get("province"));
				userInfo.put("country", userInfoJSON.get("country"));
				userInfo.put("avatarUrl", userInfoJSON.get("avatarUrl"));

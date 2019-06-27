//menu.js
//获取应用实例
const app = getApp()

Page({
  data: {
    currentSelectType: 'ziti',
    imgUrls: [
      'image/item11.jpg',
      'image/item12.jpg',
      'image/item13.jpg'
      
    ],
    indicatorDots: true, //是否显示面板指示点
    autoplay: true, //是否自动切换
    interval: 3000, //自动切换时间间隔,3s
    duration: 1000, //  滑动动画时长1s
    iconSize:[20],
    iconColor:['red'],
    iconType:['success'],
    tabIndex: 0,
    // 统计商品数量和价格
    orderCount: {
      num: 0,
      money: 0
    },
    bottomFlag: false,
    // 提交的订单
    orders: true,
    menus: [{
      id: 1,
      menu: '招牌简餐'
    }, {
      id: 4,
      menu: '佐餐饮品'
    }, {
      id: 6,
      menu: '甜点小食'
    }
    ],
    // 商品列表
    items: [{
      id: 1,
      title: '茶香排骨',
      price: 11,
      active: false,
      num: 1
    }, {
      id: 2,
      title: '番茄鸡肉丸',
      price: 12,
      active: false,
      num: 1
    }, {
      id: 3,
      title: '耳光炒饭',
      price: 15,
      active: false,
      num: 1

    }, {
      id: 4,
      title: '柠檬百香果',
      price: 18,
      active: false,
      num: 1
    }, {
      id: 5,
      title: '满杯红柚',
      price: 19,
      active: false,
      num: 1
    }, {
      id: 6,
      title: '雪花酥',
      price: 20,
      active: false,
      num: 1
    }, {
      id: 7,
      title: '芒果冰淇凌',
      price: 21,
      active: false,
      num: 1
    }]
  },
  // 下拉刷新
  onPullDownRefresh: function () {
    setTimeout(() => {
      wx.showToast({
        title: '成功加载数据',
        icon: 'success',
        duration: 500
      });
      wx.stopPullDownRefresh()
    }, 500);
  },
  tabMenu: function (event) {
    let index = event.target.dataset.index;
    this.setData({
      tabIndex: index
    });
    //requestmenudata(index);//获取对应类别菜单
  },
  // 点击去购物车结账
  card: function () {
    let that = this;
    // 判断是否有选中商品
    if (that.data.orderCount.num !== 0) {
      // 跳转到购物车订单页
      wx.redirectTo({
        url: '../order/order'
      });
    } else {
      wx.showToast({
        title: '您未选中任何商品',
        icon: 'none',
        duration: 2000
      })
    }
  }, 
  mard: function () {
    wx.redirectTo({
      url: '../menu/menu'
    })
  }, 
  ord: function () {
    wx.navigateTo({
      url: '../history/history'
    })
  },
  rard: function () {
    wx.navigateTo({
      url: '../review/review'
    })
  },
  
  tapTo: function(e){
    console.log(e)
    wx.navigateTo({
      url: '../food/' + e.currentTarget.dataset.id,
    })
  },

  addOrder: function (event) {
    let that = this;
    let id = event.target.dataset.id;
    let index = event.target.dataset.index;
    let param = this.data.items[index];
    let subOrders = []; // 购物单列表存储数据
    param.active ? param.active = false : param.active = true;
    // 改变添加按钮的状态
    this.data.items.splice(index, 1, param);
    that.setData({
      items: this.data.items
    });
    // 将已经确定的菜单添加到购物单列表
    this.data.items.forEach(item => {
      if (item.active) {
        subOrders.push(item);
      }
    });
    // 判断底部提交菜单显示隐藏
    if (subOrders.length == 0) {
      that.setData({
        bottomFlag: false
      });
    } else {
      that.setData({
        bottomFlag: true
      });
    }
    let money = 0;
    let num = subOrders.length;
    subOrders.forEach(item => {
      money += item.price; // 总价格求和
    });
    let orderCount = {
      num,
      money
    }
    // 设置显示对应的总数和全部价钱
    this.setData({
      orderCount
    });
    // 将选中的商品存储在本地
    wx.setStorage({
      key: "orders",
      data: subOrders
    });
  },

  onLoad: function () {//第一次进入读取种类
    //requestcatedata();
  }, 
  requestcatedata: function () {
    wx.request({
      url: '/v1/category/<:rid>',
      method: 'GET',
      success(res) {
        console.log(res.data);
        this.setdata({
          menus: res.data
        });
      }
    })
  },
  requestmenudata: function (category) {
    wx.request({
      url: 'v1/order/<:rid>',
      method: 'GET',
      header: {
        'type': category
      },
      success(res) {
        console.log(res.data);
        this.setdata({
          items: res
        });
      }
    })
  },

  // 更新data 切换选中状态
  selectziti: function (e) {
    this.setData({
      currentSelectType: e.currentTarget.dataset.id
    })
  },
  selecttangshi: function (e) {
    this.setData({
      currentSelectType: e.currentTarget.dataset.id
    })
  }
})
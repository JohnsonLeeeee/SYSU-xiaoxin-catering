const app = getApp()
Page({
  data: {
    items: [{
      id: 3,
      title: '耳光炒饭',
      price: 15,
      active: false,
      num: 1,
      imgUrl: '../menu/image/item3.jpg'
    }]
  }, onShareAppMessage: function (res) {
    return {
      title: '快来尝尝这道菜吧！',
      path: '/page/user?id=123',
      success: function (res) {
        wx.showModal({
          title: '提示',
          content: '转发成功',
        })
      },
      fail: function (res) {
        wx.showModal({
          title: '提示',
          content: '转发失败',
        })
      }
    }
  }
})
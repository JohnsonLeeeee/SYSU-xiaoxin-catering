const app = getApp()
Page({
  data: {
      items: [{
      id: 5,
      title: '满杯红柚',
      price: 19,
      active: false,
      num: 1,
        imgUrl: '../menu/image/item5.jpg'
    }]
  },
  onShareAppMessage: function (res) {
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
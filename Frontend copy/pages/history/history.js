Page({

  /**
   * 页面的初始数据
   */
  data: {
    number: 3,
    orders: [
        [{
          image:'image/item-m.jpg',
          name: '雪花酥', 
          price: 15.0, 
          quantity: 2
        }],
        [{
          image: 'image/item-m.jpg',
          name: '芒果', 
          price: 20.0, 
          quantity: 3
        }],
        [{
          image: 'image/item-m.jpg',
          name: '雪花酥', 
          price: 15.0,
          quantity: 1
        }, 
        {
          image: 'image/item-m.jpg',
          name: '芒果', 
          price: 20.0, 
          quantity: 1
        }]
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  },
  gotomenu: function () {
    wx.navigateTo({
      url: '../menu/menu'
    })
  }
})
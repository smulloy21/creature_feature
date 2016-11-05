var mongoose = require('mongoose');

module.exports = new mongoose.Schema({
  email: { type: String, required: true, lowercase: true },
  password: { type: String, required: true, },
  victories: [{
      name: { type: String },
      achieved: { type: Date }
  }],
  goals: [{
    status: { type: String, enum: ['created', 'completed'], required: true},
    completedTime: { type: Date }
  }],
  monster: {
    name: { type: String },
    level: { type: Number, min: 1, max: 7 }
  },
  friends: [ { type: mongoose.Schema.Types.ObjectId, ref: 'User'} ],
  data: {
    oauth: { type: String, required: true }
  }
});

module.exports.set('toObject', { virtuals: true });
module.exports.set('toJSON', { virtuals: true });

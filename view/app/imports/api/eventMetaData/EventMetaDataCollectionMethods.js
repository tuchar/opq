import { Mongo } from 'meteor/mongo';
import { ValidatedMethod } from 'meteor/mdg:validated-method';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';
import { EventMetaData } from './EventMetaDataCollection.js';
import Moment from 'moment';
import { demapify } from 'es6-mapify';
import { timeUnitString } from "../../utils/utils.js";

export const eventMetaDataCount = new ValidatedMethod({
  name: 'EventMetaData.eventMetaDataCount',
  validate: new SimpleSchema({
    startTime: {type: Date},
    endTime: {type: Date, optional: true}
  }).validator({clean: true}),
  run({ startTime, endTime }) {
    const selector = EventMetaData.queryConstructors().getEventMetaData({ startTime, endTime });
    const eventMetaData = EventMetaData.find(selector, {});
    return eventMetaData.count();
  }
});

export const eventMetaDataCountMap = new ValidatedMethod({
  name: 'EventMetaData.eventMetaDataCountMap',
  validate: new SimpleSchema({
    timeUnit: {type: String},
    startTime: {type: Number},
    endTime: {type: Number, optional: true}
  }).validator({clean: true}),
  run({ timeUnit, startTime, endTime }) {
    // TimeUnits can be year, month, week, day, dayOfMonth, hourOfDay
    const selector = EventMetaData.queryConstructors().getEventMetaData({ startTime, endTime });
    const eventMetaData = EventMetaData.find(selector, {});

    const eventCountMap = new Map();
    eventMetaData.forEach(event => {
      const timeUnitKey = timeUnitString(event.event_start, timeUnit);
      (eventCountMap.has(timeUnitKey)) ? eventCountMap.set(timeUnitKey, eventCountMap.get(timeUnitKey) + 1)
                                       : eventCountMap.set(timeUnitKey, 1);
    });

    return demapify(eventCountMap);
  }
});

export const getEventMetaDataById = new ValidatedMethod({
  name: 'EventMetaData.getEventMetaDataById',
  validate: new SimpleSchema({
    eventMetaDataId: {type: Mongo.ObjectID}
  }).validator({clean: true}),
  run({ eventMetaDataId }) {
    const eventMetaData = EventMetaData.findOne({_id: eventMetaDataId}, {});
    return eventMetaData;
  }
});

export const getMostRecentEventMetaData = new ValidatedMethod({
  name: 'EventMetaData.getMostRecentEventMetaData',
  validate: new SimpleSchema({}).validator({clean: true}),
  run() {
    const mostRecentEvent = EventMetaData.findOne({}, {sort: {event_start: -1}});
    return mostRecentEvent;
  }
});
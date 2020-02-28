import {ai} from './scripts'
import {control} from './scripts'
import {game} from './scripts'
// setup(function(){
//   ul = $('<ul><li class="no-results"></li></ul>');
// });

// test('constructor', function () {
//   var l = new Likes(ul);
//   assert(l);
// });
QUnit.test( "hello test", function( assert ) {
    assert.ok( x == "x", "won!" );
  });
  QUnit.test("prettydate basics", function( assert ) {
    var now = "2008/01/28 22:25:00";
    assert.equal(prettyDate(now, "2008/01/28 22:24:30"), "just now");
    assert.equal(prettyDate(now, "2008/01/28 22:23:30"), "1 minute ago");
    assert.equal(prettyDate(now, "2008/01/28 21:23:30"), "1 hour ago");
    assert.equal(prettyDate(now, "2008/01/27 22:23:30"), "Yesterday");
    assert.equal(prettyDate(now, "2008/01/26 22:23:30"), "2 days ago");
    assert.equal(prettyDate(now, "2007/01/26 22:23:30"), undefined);
  });
insert into contest (cid, contestname, activatetime, starttime, endtime, activatetime_string, endtime_string) values
    (3, "contest", "2014-03-15 00:00:00", "2014-03-15 13:30:00", "2014-03-15 17:00:00",
        "2014-03-15 13:30:00", "2014-03-15 17:00:00");

insert into team (login, name, categoryid) values
    ("foo", "The Foo Team", 2),
    ("bar", "The Bar Team", 2);

insert into problem (probid, cid, name) values
    ("A", 3, "Problem A");

insert into submission (submitid, cid, teamid, probid, langid, submittime) values
    (1, 3, "foo", "A", "c", "2014-03-15 13:45:55"),
    (2, 3, "foo", "A", "c", "2014-03-15 13:55:55"),
    (3, 3, "bar", "A", "cpp", "2014-03-15 14:05:55"),
    (4, 3, "bar", "A", "cpp", "2014-03-15 14:15:55");

insert into judging (judgingid, cid, submitid, starttime, endtime, result) values
    (1, 3, 1, "2014-03-15 13:45:56", "2014-03-15 13:45:57", "wrong-answer"),
    (2, 3, 2, "2014-03-15 13:55:56", "2014-03-15 13:55:57", "wrong-answer"),
    (3, 3, 3, "2014-03-15 14:05:56", "2014-03-15 14:05:57", "wrong-answer"),
    (4, 3, 4, "2014-03-15 14:15:56", "2014-03-15 14:15:57", "accepted");

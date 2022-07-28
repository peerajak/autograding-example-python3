import main;

def test_hello():
    monkeypatch.setattr('sys.stdin', io.StringIO('2wf rwf e3rtg3 f 53tt3 er y'))
    main()
    captured = capsys.readouterr()
    output = captured.out
    assert output == "2wf 53tt3 e3rtg3 er f rwf y"

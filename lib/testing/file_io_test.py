from file_io import write_file, append_file, read_file
import pytest

def test_write_file(tmp_path):
    """Test write_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_name, file_content)
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content

def test_append_file(tmp_path):
    """Test append_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    append_content = "Appended content."
    write_file(file_name, file_content)
    append_file(file_name, append_content)
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    
    assert file_content_read == file_content + "\n" + append_content

def test_read_file(tmp_path):
    """Test read_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_name, file_content)
    file_content_read = read_file(file_name)
    assert file_content_read == file_content

def test_write_file_overwrites(tmp_path):
    """Test that write_file overwrites existing content"""
    file_name = tmp_path / "overwrite_file"
    write_file(file_name, "First content.")
    write_file(file_name, "Second content.")
    with open(f'{file_name}.txt', 'r') as f:
        assert f.read() == "Second content."

def test_append_file_multiple_times(tmp_path):
    """Test appending multiple times"""
    file_name = tmp_path / "multi_append"
    write_file(file_name, "Line1")
    append_file(file_name, "Line2")
    append_file(file_name, "Line3")
    with open(f'{file_name}.txt', 'r') as f:
        assert f.read() == "Line1\nLine2\nLine3"

def test_write_and_read_empty_content(tmp_path):
    """Test writing and reading empty content"""
    file_name = tmp_path / "empty_content"
    write_file(file_name, "")
    assert read_file(file_name) == ""

def test_append_to_empty_file(tmp_path):
    """Test appending to an empty file"""
    file_name = tmp_path / "empty_append"
    write_file(file_name, "")
    append_file(file_name, "Appended only.")
    with open(f'{file_name}.txt', 'r') as f:
       
        assert f.read() == "Appended only."

def test_read_file_nonexistent(tmp_path):
    """Test reading a non-existent file raises FileNotFoundError"""
    file_name = tmp_path / "does_not_exist"
    with pytest.raises(FileNotFoundError):
        read_file(file_name)

    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    append_content = "Appended content."
    write_file(file_name, file_content)
    append_file(file_name, append_content)
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content + "\n" + append_content
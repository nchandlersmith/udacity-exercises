from file_system import File, Directory
import pytest


class TestFileSystemComponent:
    def test_file_(self):
        file = File('test_file.txt', 100)
        assert file.show_details() == "test_file.txt 100 kB"
        assert file.get_size() == 100

    def test_file_with_indent(self):
        file = File('test_file.txt', 100)
        assert file.show_details(indent=4) == "    test_file.txt 100 kB"

    def test_directory_add_component_adds_a_component(self):
        directory = Directory('test_directory', 0)
        file = File('test_file.txt', 100)
        directory.add_component(file)
        assert len(directory._components) == 1
        assert directory._components[0] is file
        
    def test_directory_get_size_returns_size_of_containing_files(self):
        directory = Directory('test_directory', 0)
        file1 = File('file1.txt', 100)
        file2 = File('file2.txt', 200)
        directory.add_component(file1)
        directory.add_component(file2)
        assert directory.get_size() == 300
        
    def test_directory_show_details(self):
        directory = Directory('test_directory', 0)
        file1 = File('file1.txt', 100)
        file2 = File('file2.txt', 200)
        directory.add_component(file1)
        directory.add_component(file2)
        expected_details = "test_directory 300 kB\n  file1.txt 100 kB\n  file2.txt 200 kB"
        assert directory.show_details() == expected_details
        
    def test_directory_with_hierarchy(self):
        root_directory = Directory('root_directory', 0)
        sub_directory = Directory('sub_directory', 0)
        file1 = File('file1.txt', 100)
        file2 = File('file2.txt', 200)
        sub_directory.add_component(file1)
        root_directory.add_component(sub_directory)
        root_directory.add_component(file2)
        expected_details = "root_directory 300 kB\n  sub_directory 100 kB\n    file1.txt 100 kB\n  file2.txt 200 kB"
        assert root_directory.show_details() == expected_details

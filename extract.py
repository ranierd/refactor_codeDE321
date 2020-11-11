class Extract:

    def get_data(self, file_path):
        all_lines = []
        assert (file_path is not None)
        assert file_path != ''
        file = open(file_path, 'r')
        for line in file:
            all_lines.append(line)
        file.close()
        return all_lines


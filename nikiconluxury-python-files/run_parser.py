from brand_parser import JimmyChooParser


# ##START FENDI PARSER##
output_directory_path = 'parser-output'
directory_path = 'jimmy_choo'
jimmychoo_parser = JimmyChooParser(output_directory_path)
jimmychoo_parser.parse_directory(directory_path)
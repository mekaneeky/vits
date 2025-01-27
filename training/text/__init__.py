# """ from https://github.com/keithito/tacotron """
# from text import cleaners
# #from text.symbols import symbols


# class TextMapper(object):
#     def __init__(self, vocab_file):
#         self.symbols = [x.replace("\n", "") for x in open(vocab_file, encoding="utf-8").readlines()]
#         self.SPACE_ID = self.symbols.index(" ")
#         self._symbol_to_id = {s: i for i, s in enumerate(self.symbols)}
#         self._id_to_symbol = {i: s for i, s in enumerate(self.symbols)}

#     def text_to_sequence(self, text, cleaner_names):
#         '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
#         Args:
#         text: string to convert to a sequence
#         cleaner_names: names of the cleaner functions to run the text through
#         Returns:
#         List of integers corresponding to the symbols in the text
#         '''
#         sequence = []
#         clean_text = text.strip()
#         for symbol in clean_text:
#             symbol_id = self._symbol_to_id[symbol]
#             sequence += [symbol_id]
#         return sequence

#     def uromanize(self, text, uroman_pl):
#         iso = "xxx"
#         with tempfile.NamedTemporaryFile() as tf, \
#              tempfile.NamedTemporaryFile() as tf2:
#             with open(tf.name, "w") as f:
#                 f.write("\n".join([text]))
#             cmd = f"perl " + uroman_pl
#             cmd += f" -l {iso} "
#             cmd +=  f" < {tf.name} > {tf2.name}"
#             os.system(cmd)
#             outtexts = []
#             with open(tf2.name) as f:
#                 for line in f:
#                     line =  re.sub(r"\s+", " ", line).strip()
#                     outtexts.append(line)
#             outtext = outtexts[0]
#         return outtext

#     def get_text(self, text, hps):
#         text_norm = self.text_to_sequence(text, hps.data.text_cleaners)
#         if hps.data.add_blank:
#             text_norm = commons.intersperse(text_norm, 0)
#         text_norm = torch.LongTensor(text_norm)
#         return text_norm

#     def filter_oov(self, text):
#         val_chars = self._symbol_to_id
#         txt_filt = "".join(list(filter(lambda x: x in val_chars, text)))
#         #print(f"text after filtering OOV: {txt_filt}")
#         return txt_filt

# def preprocess_text(txt, text_mapper, hps, uroman_dir=None, lang=None):
#     txt = preprocess_char(txt, lang=lang)
#     is_uroman = hps.data.training_files.split('.')[-1] == 'uroman'
#     if is_uroman:
#         with tempfile.TemporaryDirectory() as tmp_dir:
#             if uroman_dir is None:
#                 cmd = f"git clone git@github.com:isi-nlp/uroman.git {tmp_dir}"
#                 print(cmd)
#                 subprocess.check_output(cmd, shell=True)
#                 uroman_dir = tmp_dir
#             uroman_pl = os.path.join(uroman_dir, "bin", "uroman.pl")
#             print(f"uromanize")
#             txt = text_mapper.uromanize(txt, uroman_pl)
#             print(f"uroman text: {txt}")
#     txt = txt.lower()
#     txt = text_mapper.filter_oov(txt)
#     return txt


# # Mappings from symbol to numeric ID and vice versa:
# mapper = TextMapper("ach/vocab.txt")
# _symbol_to_id = mapper._symbol_to_id#{s: i for i, s in enumerate(symbols)}
# _id_to_symbol = mapper._id_to_symbol#{i: s for i, s in enumerate(symbols)}


# def preprocess_text(txt, text_mapper, hps, uroman_dir=None, lang=None):
#     txt = preprocess_char(txt, lang=lang)
#     is_uroman = hps.data.training_files.split('.')[-1] == 'uroman'
#     if is_uroman:
#         with tempfile.TemporaryDirectory() as tmp_dir:
#             if uroman_dir is None:
#                 cmd = f"git clone git@github.com:isi-nlp/uroman.git {tmp_dir}"
#                 print(cmd)
#                 subprocess.check_output(cmd, shell=True)
#                 uroman_dir = tmp_dir
#             uroman_pl = os.path.join(uroman_dir, "bin", "uroman.pl")
#             print(f"uromanize")
#             txt = text_mapper.uromanize(txt, uroman_pl)
#             print(f"uroman text: {txt}")
#     txt = txt.lower()
#     txt = text_mapper.filter_oov(txt)
#     return txt


# def text_to_sequence(text, cleaner_names):
#   '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
#     Args:
#       text: string to convert to a sequence
#       cleaner_names: names of the cleaner functions to run the text through
#     Returns:
#       List of integers corresponding to the symbols in the text
#   '''
#   sequence = []

#   clean_text = _clean_text(text, cleaner_names)
#   for symbol in clean_text:
#     symbol_id = _symbol_to_id[symbol]
#     sequence += [symbol_id]
#   return sequence


# def cleaned_text_to_sequence(cleaned_text):
#   '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
#     Args:
#       text: string to convert to a sequence
#     Returns:
#       List of integers corresponding to the symbols in the text
#   '''
#   sequence = [_symbol_to_id[symbol] for symbol in cleaned_text]
#   return sequence


# def sequence_to_text(sequence):
#   '''Converts a sequence of IDs back to a string'''
#   result = ''
#   for symbol_id in sequence:
#     s = _id_to_symbol[symbol_id]
#     result += s
#   return result


# def _clean_text(text, cleaner_names):
#   for name in cleaner_names:
#     cleaner = getattr(cleaners, name)
#     if not cleaner:
#       raise Exception('Unknown cleaner: %s' % name)
#     text = cleaner(text)
#   return text

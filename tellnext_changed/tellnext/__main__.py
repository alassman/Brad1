import tellnext_changed.tellnext.tool
import tellnext_changed.tellnext.model
import tellnext_changed.tellnext.store as store
import time

#tellnext_model.MarkovModel(store=store.SQLiteStore(path='MODEL.db'))

if __name__ == '__main__':
	# start_time = time.time()
	# words_list = ['i', 'am']
	# tellnext_changed.tellnext.tool.update_model('i', None, 'brad')
	# print(tellnext_changed.tellnext.tool.new_next_word(words_list[0], words_list[1]))
	
	
	# elapsed_time = time.time() - start_time
	# print(elapsed_time)

	tellnext_changed.tellnext.tool.main()
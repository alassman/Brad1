import tellnext_changed.tellnext.tool
import tellnext_changed.tellnext.model
import tellnext_changed.tellnext.store as store

#tellnext_model.MarkovModel(store=store.SQLiteStore(path='MODEL.db'))

if __name__ == '__main__':
	words_list = ['i', 'am']
	model = tellnext_changed.tellnext.model.MarkovModel(store=store.SQLiteStore(path='MODEL.db'))
	tellnext_changed.tellnext.tool.new_next_word(words_list[0], words_list[1], model)
	tellnext_changed.tellnext.tool.update_model('i', 'am', 'brad', model)

	#tellnext_changed.tellnext.tool.main()
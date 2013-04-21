
$(function() {
  function start(books) {

    var $inputSearch = $('#inputSearch'),
        $result = $('#results'),

        $authorCheckbox = $('#restName'),
        $titleCheckbox = $('#ranking'),
        //$caseCheckbox = $('#case'),

        searchAuthors = false,
        searchTitles = false,
        //isCaseSensitive = false,
		
        fuse;

    function search() {
      var r = fuse.search($inputSearch.val());
      $result.empty();
      $.each(r, function() {
			$result.append('<a href="http://127.0.0.1:8000/users/restaurantProfile/' + this.id + ' "><div class="result-item"> ' +   ' <img src=" ' + this.image +' " alt="Image not found" onError = "{{ STATIC_PREFIX }}/img/ad.jpg" width="200" height="200" /> </a> ' + '<p>' + this.name  + ' , ' + this.ranking + '</p></div>');
	  });
    }
	
	
    function createFuse() {
      var keys = [];
      if (searchAuthors) {
        keys.push('name');
      }
      if (searchTitles) {
        keys.push('ranking');
      }
      fuse = new Fuse(books, {
        keys: keys,
        caseSensitive: false
      });
    }

    function onAuthorCheckboxChanged() {
      searchAuthors= $authorCheckbox.prop('checked');
      createFuse();
      search();
    }

    function onTitleCheckboxChanged() {
      searchTitles = $titleCheckbox.prop('checked');
      createFuse();
      search();
    }

    //function onCaseCheckboxChanged() {
      //isCaseSensitive = $caseCheckbox.prop('checked');
      //createFuse();
      //search();
    //}

    $authorCheckbox.on('change', onAuthorCheckboxChanged);
    $titleCheckbox.on('change', onTitleCheckboxChanged);
    //$caseCheckbox.on('change', onCaseCheckboxChanged);

    $inputSearch.on('keyup', search);

    createFuse();
  }

  

  $.getJSON('http://127.0.0.1:8000/users/rlist/', function(data) {

     start(data);
  });

});

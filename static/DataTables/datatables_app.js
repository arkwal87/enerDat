function tableKwargs(order, sort) {
    return {
        "language": {
            "sProcessing":   "Przetwarzanie...",
	        "sLengthMenu":   "Pokaż _MENU_ pozycji",
	        "sZeroRecords":  "Nie znaleziono pasujących pozycji",
	        "sInfoThousands":  " ",
	        "sInfo":         "Pozycje od _START_ do _END_ z _TOTAL_ łącznie",
	        "sInfoEmpty":    "Pozycji 0 z 0 dostępnych",
	        "sInfoFiltered": "(filtrowanie spośród _MAX_ dostępnych pozycji)",
	        "sInfoPostFix":  "",
	        "sSearch":       "Szukaj:",
	        "sUrl":          "",
	        "oPaginate": {
		        "sFirst":    "Pierwsza",
		        "sPrevious": "Poprzednia",
                "sNext":     "Następna",
                "sLast":     "Ostatnia"
                },
            "sEmptyTable":     "Brak danych",
            "sLoadingRecords": "Wczytywanie...",
            "oAria": {
                "sSortAscending":  ": aktywuj, by posortować kolumnę rosnąco",
                "sSortDescending": ": aktywuj, by posortować kolumnę malejąco"
                }
            },
        "order": [[order, sort]]
    }
}

$(document).ready(function() {
    $('#detailTable').DataTable(tableKwargs(0,"asc"));
    $('#listTable').DataTable(tableKwargs(0,"desc"));
    $('#contractsTable').DataTable(tableKwargs(0,"asc"));
    $('#a1Table').DataTable(tableKwargs(0,"desc"));
})
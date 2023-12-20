function navigate_to_link(url)
{
    window.location.href=url;
}

function search_query(query)
{
    var url = '/entities/search/' + query;
    window.location.href = url;
}
import PlacesAutocomplete, {
    geocodeByAddress,
    getLatLng
  } from "react-places-autocomplete";

  import React from "react";
  
  export default function Address(props) {
    const [address, setAddress] = React.useState("");
    const [coordinates, setCoordinates] = React.useState({
      lat: null,
      lng: null
    });
    const handleSelect = async value => {
      const results = await geocodeByAddress(value);
      const latLng = await getLatLng(results[0]);
      setAddress(value);
      setCoordinates(latLng);
      props.returnLocation(value)
      console.log(value)
    };
  
    return (
      <div style={{position:"absolute"}}>
        <PlacesAutocomplete
          value={address}
          onChange={setAddress}
          onSelect={handleSelect}
          
        >
          {({ getInputProps, suggestions, getSuggestionItemProps, loading }) => (
            <div>
         
  
              <input {...getInputProps({ placeholder: "Type address" })} />
  
              <div>
                {loading ? <div>...loading</div> : null}
  
                {suggestions.map(suggestion => {
                  const style = {
                    backgroundColor: suggestion.active ? "#41b6e6" : "#fff"
                  };
  
                  return (
                    <div {...getSuggestionItemProps(suggestion, { style })}>
                      {suggestion.description}
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </PlacesAutocomplete>
      </div>
    );
  }
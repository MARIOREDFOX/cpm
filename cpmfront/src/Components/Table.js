import React from 'react';

const Table = ({ droplets }) => {
  return (
    <table className="table table-bordered mt-4">
      <thead>
        <tr>
        <th>Name</th>
         <th>One</th>
          <th>Gender</th>
          <th>Age</th>
          <th>Levy cash</th>
          <th>Period of joining</th>
          <th>Category</th>
          <th>classes</th>
          <th>Qualification</th>
          <th>Income</th>
          <th>Socio culture cast</th>
          <th>Minority</th>
          <th>Organisation CPM</th>
          <th>Disability</th>
          <th>News letter</th>

        </tr>
      </thead>
      <tbody>
        {(droplets.length > 0) ? droplets.map((droplet, index) => {
          return (
            <tr key={index}>
              <td>{droplet.name}</td>
              <td>{droplet.one}</td>
              <td>{droplet.gender}</td>
              <td>{droplet.age}</td>
              <td>{droplet.levy_cash}</td>
              <td>{droplet.period_of_joining}</td>
              <td>{droplet.category}</td>
              <td>{droplet.classes}</td>
              <td>{droplet.qualification}</td>
              <td>{droplet.income}</td>
              <td>{droplet.socio_culture_caste}</td>
              <td>{droplet.minority}</td>
              <td>{droplet.organisation_cpm}</td>
              <td>{droplet.disability}</td>
              <td>{droplet.news_letter}</td>
              
            </tr>
          )
        }) : <tr><td colSpan="5">Loading...</td></tr>}
      </tbody>
    </table>
  );
}

export default Table
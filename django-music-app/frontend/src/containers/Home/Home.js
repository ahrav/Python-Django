import React from 'react';
import { NavLink, Route, Switch } from 'react-router-dom';
import NewSong from '../../components/Songs/NewSong'
import Songs from '../../components/Songs/Songs'
import SongDetail from '../../components/SongDetail/SongDetail'
import './Home.css'

const Home = props => {

    return (
    <React.Fragment>
      <header className="Header">
          <nav>
              <ul>
                  <li><NavLink
                        to="/songs/"
                        exact
                        activeStyle={{
                            color: '#fa923f',
                            textDecoration: 'underline'
                        }}>Songs
                      </NavLink></li>
                  <li><NavLink
                        to="/new-song/"
                        exact
                        activeStyle={{
                            color: '#fa923f',
                            textDecoration: 'underline'
                        }}>Add Song
                      </NavLink></li>
              </ul>
          </nav>
      </header>
      <Switch>
          <Route path="/new-song" exact component={NewSong}/>
          <Route path="/songs" exact component={Songs}/>
          <Route path="/songs/:songId" exact render={props => <SongDetail {...props} />}/>
      </Switch>
    </React.Fragment>
    )
}

export default Home
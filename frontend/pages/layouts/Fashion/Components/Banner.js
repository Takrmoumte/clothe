import React, { Fragment } from "react";
import Slider from "react-slick";
import Link from "next/link";
import { Container, Row, Col } from "reactstrap";
import MasterBanner from "./MasterBanner";
const Data = [
  {
    img: "home24",
    title: "location de",
    desc: "robes de mariage",
    link: "/left-sidebar/collection ",
    color: "white "
    
  },
  {
    img: "home26",
    title: "robes location de",
    desc: "robes traditionnelles",
    link: "/left-sidebar/collection ",
    color: "white "
  },
  {
    img: "home27",
    title: "location de ",
    desc: "robes classiques",
    link: "/left-sidebar/collection ",
    color: "white "
  },
  {
      img: "home28",
      title: "Location de",
      desc: "robes de soirée",
      link: "/left-sidebar/collection ",
      color: "white "
    },
    {
      img: "home25",
      title: "location de",
      desc: "Accesoires & chaussures",
      link: "/left-sidebar/collection ",
      color: "white "
    },
];

const Banner = () => {
  return (
    <Fragment>
      <section className="p-0">
        <Slider className="slide-1 home-slider">
          {Data.map((data, i) => {
            return (
              <MasterBanner
                key={i}
                img={data.img}
                desc={data.desc}
                title={data.title}
                link={data.link}
                color={data.color}
              />
            );
          })}
        </Slider>
      </section>
    </Fragment>
  );
};

export default Banner;

import { ConnectButton } from "@rainbow-me/rainbowkit";
import Head from "next/head";
import styles from "../styles/Home.module.css";
// import { publicProvider } from 'wagmi/providers/public';
import {
  FixedRateExchange
} from "@oceanprotocol/lib";

// let freAddress = "0x000"
// let freId = "0x000"

// const FRE_NFT_NAME = 'Datatoken 2'
// const FRE_NFT_SYMBOL = 'DT2'

// const fixedRate = new FixedRateExchange(freAddress, web3)
// const oceanAmount = await (
//   await fixedRate.calcBaseInGivenDatatokensOut(freId, '1')
// ).baseTokenAmount

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>OceanKit Demo</title>
        <meta
          name="description"
          content="Demo app part of a tutorial on adding RainbowKit to a React application"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title} style={{ marginBottom: "4rem" }}>
          Welcome to this demo of{" "}
          <a href="https://www.rainbowkit.com/">OceanKit</a>
        </h1>
        <ConnectButton />
      </main>
    </div>
  );
}

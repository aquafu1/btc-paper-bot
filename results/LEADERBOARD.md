# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1090 windows, 30162 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 570 | 34.6 | 35.0 | $-327.96 | -5.8% | $672.04 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3048 | 51.1 | 50.5 | $-872.51 | -2.9% | $127.49 | -1.6 | done | can't tell from luck |
| value_ev10 | 1399 | 38.0 | 39.1 | $-888.24 | -6.3% | $111.76 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2562 | 49.8 | 49.4 | $-1043.09 | -4.1% | $-43.09 | -2.1 | done | losing for real |
| value_ev5 | 2125 | 40.0 | 41.0 | $-1251.11 | -5.9% | $-251.11 | -2.3 | done | losing for real |
| trend_filter | 1792 | 49.5 | 50.4 | $-1261.80 | -7.0% | $-261.80 | -3.0 | done | losing for real |
| coinflip | 4352 | 50.6 | 50.2 | $-1614.81 | -3.7% | $-614.81 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2562 | 50.2 | 51.1 | $-1717.22 | -6.7% | $-717.22 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 3048 | 48.9 | 50.2 | $-2022.27 | -6.6% | $-1022.27 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4352 | 50.9 | 51.4 | $-2159.97 | -5.0% | $-1159.97 | -3.4 | done | losing for real |
| always_up | 4352 | 47.5 | 49.3 | $-3487.04 | -8.0% | $-2487.04 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6890 | 48.5 | 49.0 | $-3356.67 |
| ETH | 7473 | 48.2 | 48.4 | $-4394.75 |
| SOL | 7862 | 48.1 | 48.4 | $-4434.11 |
| XRP | 7937 | 48.3 | 48.2 | $-4460.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

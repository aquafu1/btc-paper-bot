# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 470 windows, 12894 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 237 | 35.0 | 35.9 | $-136.40 | -5.8% | $863.60 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1093 | 50.8 | 50.0 | $-290.07 | -2.7% | $709.93 | -0.9 | done | can't tell from luck |
| value_ev10 | 609 | 39.1 | 40.1 | $-362.22 | -5.9% | $637.78 | -1.2 | done | can't tell from luck |
| trend_filter | 749 | 49.7 | 50.8 | $-461.85 | -6.2% | $538.15 | -1.7 | done | can't tell from luck |
| value_ev5 | 901 | 41.1 | 41.9 | $-493.85 | -5.5% | $506.15 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1298 | 49.8 | 50.0 | $-507.27 | -3.9% | $492.73 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1298 | 50.2 | 51.4 | $-833.41 | -6.4% | $166.59 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1093 | 49.2 | 51.4 | $-926.21 | -8.5% | $73.79 | -2.9 | done | losing for real |
| coinflip | 1872 | 49.8 | 50.8 | $-1075.84 | -5.7% | $-75.84 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1872 | 49.8 | 51.7 | $-1335.33 | -7.1% | $-335.33 | -3.2 | done | losing for real |
| always_up | 1872 | 46.5 | 50.4 | $-2148.70 | -11.5% | $-1148.70 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2915 | 47.5 | 49.3 | $-2227.55 |
| ETH | 3234 | 48.1 | 48.8 | $-2134.53 |
| SOL | 3357 | 47.7 | 49.3 | $-2487.31 |
| XRP | 3388 | 48.6 | 49.1 | $-1721.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

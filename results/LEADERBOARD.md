# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 533 windows, 14732 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1257 | 51.7 | 49.9 | $-72.51 | -0.6% | $927.49 | -0.2 | done | can't tell from luck |
| value_ev20 | 279 | 34.8 | 35.6 | $-202.64 | -7.3% | $797.36 | -0.9 | done | can't tell from luck |
| trend_filter | 863 | 50.2 | 50.8 | $-472.77 | -5.5% | $527.23 | -1.6 | done | can't tell from luck |
| value_ev10 | 688 | 38.1 | 39.8 | $-560.63 | -8.1% | $439.37 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1493 | 49.9 | 49.7 | $-562.93 | -3.8% | $437.07 | -1.5 | done | can't tell from luck |
| value_ev5 | 1027 | 40.2 | 41.5 | $-726.07 | -7.1% | $273.93 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1493 | 50.1 | 51.4 | $-1050.99 | -7.0% | $-50.99 | -2.8 | done | losing for real |
| coinflip | 2125 | 49.9 | 50.6 | $-1186.51 | -5.6% | $-186.51 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1257 | 48.3 | 51.3 | $-1294.16 | -10.3% | $-294.16 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2125 | 49.7 | 51.6 | $-1612.11 | -7.6% | $-612.11 | -3.6 | done | losing for real |
| always_up | 2125 | 46.6 | 50.1 | $-2379.88 | -11.2% | $-1379.88 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3347 | 47.5 | 49.3 | $-2685.01 |
| ETH | 3671 | 48.1 | 48.7 | $-2382.88 |
| SOL | 3838 | 47.7 | 49.0 | $-2807.37 |
| XRP | 3876 | 48.4 | 48.8 | $-2245.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

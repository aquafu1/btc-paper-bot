# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1053 windows, 29173 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 544 | 34.6 | 35.1 | $-308.54 | -5.7% | $691.46 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2955 | 51.2 | 50.4 | $-783.31 | -2.7% | $216.69 | -1.4 | done | can't tell from luck |
| value_ev10 | 1352 | 37.6 | 39.2 | $-973.39 | -7.2% | $26.61 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2485 | 49.7 | 49.6 | $-1178.14 | -4.7% | $-178.14 | -2.4 | done | losing for real |
| trend_filter | 1739 | 49.3 | 50.7 | $-1363.92 | -7.8% | $-363.92 | -3.4 | done | losing for real |
| value_ev5 | 2046 | 39.4 | 41.0 | $-1433.23 | -7.0% | $-433.23 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2485 | 50.3 | 51.0 | $-1556.08 | -6.3% | $-556.08 | -3.2 | done | losing for real |
| coinflip | 4204 | 50.5 | 50.3 | $-1704.73 | -4.1% | $-704.73 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2955 | 48.8 | 50.3 | $-2063.67 | -7.0% | $-1063.67 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4204 | 50.8 | 51.5 | $-2258.01 | -5.4% | $-1258.01 | -3.6 | done | losing for real |
| always_up | 4204 | 47.3 | 49.4 | $-3687.17 | -8.8% | $-2687.17 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6646 | 48.3 | 49.0 | $-3541.62 |
| ETH | 7220 | 48.1 | 48.5 | $-4625.29 |
| SOL | 7617 | 48.1 | 48.5 | $-4429.44 |
| XRP | 7690 | 48.2 | 48.3 | $-4713.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

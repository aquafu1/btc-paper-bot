# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 841 windows, 23116 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 424 | 33.0 | 34.9 | $-410.80 | -9.7% | $589.20 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2362 | 50.9 | 50.6 | $-884.63 | -3.7% | $115.37 | -1.8 | done | can't tell from luck |
| value_ev10 | 1053 | 37.2 | 39.2 | $-890.49 | -8.5% | $109.51 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 1947 | 49.9 | 49.7 | $-898.88 | -4.6% | $101.12 | -2.0 | done | losing for real |
| trend_filter | 1357 | 49.7 | 50.8 | $-980.66 | -7.2% | $19.34 | -2.7 | done | losing for real |
| value_ev5 | 1596 | 39.6 | 41.1 | $-1163.03 | -7.3% | $-163.03 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1947 | 50.1 | 51.1 | $-1382.83 | -7.1% | $-382.83 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2362 | 49.1 | 50.3 | $-1489.82 | -6.3% | $-489.82 | -3.1 | done | losing for real |
| coinflip | 3356 | 50.2 | 50.3 | $-1503.81 | -4.5% | $-503.81 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3356 | 51.2 | 51.7 | $-1624.37 | -4.8% | $-624.37 | -2.9 | done | losing for real |
| always_up | 3356 | 47.1 | 49.6 | $-3154.69 | -9.4% | $-2154.69 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5256 | 48.0 | 49.1 | $-3418.97 |
| ETH | 5756 | 48.0 | 48.5 | $-3991.16 |
| SOL | 6029 | 48.2 | 48.6 | $-3613.11 |
| XRP | 6075 | 48.4 | 48.5 | $-3360.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

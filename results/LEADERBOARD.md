# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 679 windows, 18817 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 354 | 34.5 | 35.0 | $-214.96 | -6.1% | $785.04 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1595 | 50.5 | 49.5 | $-398.83 | -2.5% | $601.17 | -1.0 | done | can't tell from luck |
| value_ev10 | 869 | 38.4 | 39.2 | $-515.56 | -5.9% | $484.44 | -1.4 | done | can't tell from luck |
| trend_filter | 1097 | 50.4 | 50.9 | $-561.27 | -5.1% | $438.73 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1932 | 51.4 | 51.0 | $-628.78 | -3.3% | $371.22 | -1.4 | done | can't tell from luck |
| value_ev5 | 1307 | 40.6 | 41.2 | $-672.88 | -5.1% | $327.12 | -1.6 | done | can't tell from luck |
| coinflip | 2712 | 50.1 | 50.4 | $-1208.16 | -4.5% | $-208.16 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1932 | 48.6 | 49.9 | $-1263.89 | -6.5% | $-263.89 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1595 | 49.5 | 51.3 | $-1264.83 | -7.9% | $-264.83 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2712 | 50.8 | 51.8 | $-1470.02 | -5.4% | $-470.02 | -2.9 | done | losing for real |
| always_up | 2712 | 47.4 | 49.7 | $-2365.50 | -8.7% | $-1365.50 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4276 | 48.3 | 49.2 | $-2478.09 |
| ETH | 4693 | 48.2 | 48.6 | $-2813.94 |
| SOL | 4902 | 48.2 | 48.7 | $-2851.81 |
| XRP | 4946 | 48.5 | 48.4 | $-2420.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

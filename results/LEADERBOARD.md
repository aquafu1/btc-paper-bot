# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 671 windows, 18582 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 347 | 34.3 | 35.2 | $-235.88 | -6.8% | $764.12 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1580 | 50.6 | 49.6 | $-372.48 | -2.4% | $627.52 | -0.9 | done | can't tell from luck |
| trend_filter | 1082 | 50.6 | 51.0 | $-542.42 | -5.0% | $457.58 | -1.7 | done | can't tell from luck |
| value_ev10 | 855 | 38.2 | 39.4 | $-578.43 | -6.8% | $421.57 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1905 | 51.3 | 50.8 | $-611.33 | -3.2% | $388.67 | -1.4 | done | can't tell from luck |
| value_ev5 | 1288 | 40.6 | 41.3 | $-703.79 | -5.5% | $296.21 | -1.7 | done | can't tell from luck |
| coinflip | 2680 | 50.2 | 50.4 | $-1170.75 | -4.4% | $-170.75 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1905 | 48.7 | 50.1 | $-1263.48 | -6.6% | $-263.48 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1580 | 49.4 | 51.3 | $-1295.54 | -8.2% | $-295.54 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2680 | 50.8 | 51.8 | $-1470.29 | -5.5% | $-470.29 | -2.9 | done | losing for real |
| always_up | 2680 | 47.3 | 49.7 | $-2383.05 | -8.9% | $-1383.05 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4223 | 48.3 | 49.2 | $-2541.13 |
| ETH | 4633 | 48.3 | 48.7 | $-2779.70 |
| SOL | 4837 | 48.1 | 48.8 | $-2910.15 |
| XRP | 4889 | 48.5 | 48.5 | $-2396.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

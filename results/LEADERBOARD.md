# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 652 windows, 18018 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 341 | 34.3 | 35.4 | $-247.49 | -7.3% | $752.51 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1519 | 50.6 | 49.6 | $-367.47 | -2.4% | $632.53 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1852 | 51.6 | 51.0 | $-562.75 | -3.0% | $437.25 | -1.3 | done | can't tell from luck |
| value_ev10 | 833 | 38.3 | 39.5 | $-590.22 | -7.1% | $409.78 | -1.7 | done | can't tell from luck |
| trend_filter | 1041 | 50.0 | 50.9 | $-611.51 | -5.9% | $388.49 | -1.9 | done | can't tell from luck |
| value_ev5 | 1261 | 40.8 | 41.4 | $-665.58 | -5.3% | $334.42 | -1.6 | done | can't tell from luck |
| coinflip | 2600 | 50.1 | 50.5 | $-1193.83 | -4.6% | $-193.83 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1519 | 49.4 | 51.4 | $-1245.24 | -8.2% | $-245.24 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1852 | 48.4 | 50.0 | $-1278.80 | -6.9% | $-278.80 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2600 | 50.5 | 51.7 | $-1505.85 | -5.8% | $-505.85 | -3.1 | done | losing for real |
| always_up | 2600 | 47.5 | 49.7 | $-2193.53 | -8.4% | $-1193.53 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4085 | 48.3 | 49.3 | $-2491.68 |
| ETH | 4498 | 48.2 | 48.7 | $-2735.50 |
| SOL | 4688 | 48.0 | 48.8 | $-2907.44 |
| XRP | 4747 | 48.5 | 48.6 | $-2327.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

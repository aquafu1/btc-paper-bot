# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1595 windows, 38674 settled trades, 410 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 816 | 34.4 | 35.1 | $-595.00 | -7.3% | $405.00 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3817 | 50.9 | 50.0 | $-1023.04 | -2.7% | $-23.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1925 | 38.4 | 39.0 | $-1029.67 | -5.3% | $-29.67 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 3199 | 51.1 | 50.9 | $-1461.17 | -4.6% | $-461.17 | -2.6 | done | losing for real |
| value_ev5 | 2888 | 40.4 | 41.0 | $-1470.38 | -5.1% | $-470.38 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3199 | 48.9 | 49.2 | $-1745.71 | -5.5% | $-745.71 | -3.1 | done | losing for real |
| trend_filter | 2273 | 48.4 | 50.3 | $-2036.82 | -9.0% | $-1036.82 | -4.4 | done | losing for real |
| coinflip | 5580 | 50.1 | 49.9 | $-2308.56 | -4.1% | $-1308.56 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3817 | 49.1 | 50.2 | $-2341.64 | -6.1% | $-1341.64 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5580 | 50.1 | 51.3 | $-3508.93 | -6.3% | $-2508.93 | -4.8 | done | losing for real |
| always_up | 5580 | 48.2 | 49.1 | $-3577.75 | -6.4% | $-2577.75 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10273 | 48.0 | 48.6 | $-5815.50 |
| ETH | 11091 | 48.0 | 47.7 | $-5698.95 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

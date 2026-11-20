# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 940 windows, 25999 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 477 | 35.0 | 34.8 | $-165.74 | -3.5% | $834.26 | -0.6 | done | can't tell from luck |
| value_ev10 | 1176 | 38.1 | 39.1 | $-666.59 | -5.7% | $333.41 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2657 | 51.1 | 50.6 | $-857.25 | -3.2% | $142.75 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2222 | 50.1 | 49.9 | $-943.22 | -4.2% | $56.78 | -2.0 | done | losing for real |
| trend_filter | 1546 | 49.9 | 51.0 | $-1088.97 | -7.0% | $-88.97 | -2.9 | done | losing for real |
| value_ev5 | 1786 | 39.7 | 41.0 | $-1123.09 | -6.3% | $-123.09 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2222 | 49.9 | 50.9 | $-1555.23 | -7.0% | $-555.23 | -3.4 | done | losing for real |
| coinflip | 3752 | 50.4 | 50.4 | $-1575.03 | -4.2% | $-575.03 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2657 | 48.9 | 50.3 | $-1761.87 | -6.6% | $-761.87 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3752 | 50.9 | 51.6 | $-1949.05 | -5.2% | $-949.05 | -3.3 | done | losing for real |
| always_up | 3752 | 46.7 | 49.7 | $-3876.77 | -10.3% | $-2876.77 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5927 | 48.1 | 49.1 | $-3509.85 |
| ETH | 6465 | 48.2 | 48.6 | $-4056.98 |
| SOL | 6781 | 48.1 | 48.6 | $-4022.36 |
| XRP | 6826 | 48.3 | 48.5 | $-3973.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

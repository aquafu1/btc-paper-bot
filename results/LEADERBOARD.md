# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1321 windows, 35004 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 689 | 34.4 | 35.3 | $-497.07 | -7.2% | $502.93 | -1.4 | done | can't tell from luck |
| value_ev10 | 1689 | 38.8 | 39.2 | $-769.05 | -4.6% | $230.95 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3507 | 50.8 | 50.2 | $-1057.68 | -3.0% | $-57.68 | -1.8 | done | can't tell from luck |
| value_ev5 | 2547 | 40.5 | 41.1 | $-1246.98 | -4.9% | $-246.98 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2941 | 49.4 | 49.4 | $-1397.12 | -4.8% | $-397.12 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2941 | 50.6 | 50.9 | $-1575.00 | -5.4% | $-575.00 | -3.0 | done | losing for real |
| trend_filter | 2084 | 48.8 | 50.5 | $-1763.38 | -8.5% | $-763.38 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3507 | 49.2 | 50.2 | $-2161.57 | -6.2% | $-1161.57 | -3.7 | done | losing for real |
| coinflip | 5033 | 49.9 | 50.0 | $-2355.21 | -4.7% | $-1355.21 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5033 | 50.3 | 51.4 | $-2983.33 | -5.9% | $-1983.33 | -4.3 | done | losing for real |
| always_up | 5033 | 47.8 | 49.3 | $-3707.83 | -7.4% | $-2707.83 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8511 | 47.9 | 48.8 | $-5103.64 |
| ETH | 9183 | 48.2 | 48.2 | $-4826.34 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

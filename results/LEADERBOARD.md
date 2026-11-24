# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 3:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1279 windows, 34321 settled trades, 417 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 671 | 34.1 | 35.3 | $-520.36 | -7.8% | $479.64 | -1.5 | done | can't tell from luck |
| value_ev10 | 1646 | 38.6 | 39.2 | $-820.65 | -5.0% | $179.35 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3442 | 50.7 | 50.2 | $-1178.77 | -3.4% | $-178.77 | -2.0 | done | losing for real |
| value_ev5 | 2489 | 40.5 | 41.1 | $-1272.01 | -5.1% | $-272.01 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2877 | 49.5 | 49.4 | $-1343.43 | -4.7% | $-343.43 | -2.5 | done | losing for real |
| trend_filter | 2033 | 49.0 | 50.5 | $-1623.73 | -8.0% | $-623.73 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2877 | 50.5 | 51.0 | $-1647.84 | -5.7% | $-647.84 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3442 | 49.3 | 50.3 | $-2058.17 | -6.0% | $-1058.17 | -3.5 | done | losing for real |
| coinflip | 4948 | 49.9 | 50.1 | $-2295.16 | -4.6% | $-1295.16 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4948 | 50.5 | 51.4 | $-2775.47 | -5.6% | $-1775.47 | -4.1 | done | losing for real |
| always_up | 4948 | 47.8 | 49.3 | $-3649.88 | -7.4% | $-2649.88 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8181 | 48.0 | 48.9 | $-4827.63 |
| ETH | 8830 | 48.2 | 48.3 | $-4773.61 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

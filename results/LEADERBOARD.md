# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 2:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1656 windows, 39451 settled trades, 369 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 841 | 34.4 | 35.2 | $-631.08 | -7.5% | $368.92 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3875 | 50.8 | 49.9 | $-1034.04 | -2.7% | $-34.04 | -1.7 | done | can't tell from luck |
| value_ev10 | 1987 | 38.2 | 39.0 | $-1167.41 | -5.9% | $-167.41 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3242 | 51.1 | 50.9 | $-1436.36 | -4.4% | $-436.36 | -2.6 | done | losing for real |
| value_ev5 | 2967 | 40.2 | 41.0 | $-1660.10 | -5.6% | $-660.10 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3242 | 48.9 | 49.2 | $-1822.51 | -5.6% | $-822.51 | -3.2 | done | losing for real |
| trend_filter | 2310 | 48.3 | 50.4 | $-2134.47 | -9.2% | $-1134.47 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3875 | 49.2 | 50.2 | $-2351.12 | -6.1% | $-1351.12 | -3.8 | done | losing for real |
| coinflip | 5704 | 49.9 | 49.9 | $-2524.67 | -4.4% | $-1524.67 | -3.4 | done | losing for real |
| always_up | 5704 | 48.3 | 49.0 | $-3508.00 | -6.2% | $-2508.00 | -4.6 | done | losing for real |
| momentum_5m_0.00pct | 5704 | 50.2 | 51.3 | $-3523.27 | -6.2% | $-2523.27 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10626 | 47.9 | 48.5 | $-6046.87 |
| ETH | 11515 | 47.9 | 47.6 | $-6161.93 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

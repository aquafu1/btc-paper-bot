# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 890 windows, 24555 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 461 | 35.6 | 34.9 | $-99.37 | -2.2% | $900.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1127 | 38.2 | 39.1 | $-607.59 | -5.4% | $392.41 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2073 | 50.0 | 49.8 | $-908.30 | -4.4% | $91.70 | -2.0 | done | losing for real |
| trend_filter | 1445 | 50.0 | 51.0 | $-971.24 | -6.7% | $28.76 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 2508 | 50.5 | 50.4 | $-1007.92 | -4.0% | $-7.92 | -2.0 | done | losing for real |
| value_ev5 | 1704 | 39.8 | 41.0 | $-1031.18 | -6.1% | $-31.18 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2073 | 50.0 | 50.9 | $-1382.60 | -6.7% | $-382.60 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2508 | 49.5 | 50.4 | $-1392.56 | -5.6% | $-392.56 | -2.8 | done | losing for real |
| coinflip | 3552 | 50.3 | 50.3 | $-1478.56 | -4.2% | $-478.56 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 3552 | 51.3 | 51.7 | $-1612.37 | -4.5% | $-612.37 | -2.8 | done | losing for real |
| always_up | 3552 | 46.9 | 49.6 | $-3461.68 | -9.7% | $-2461.68 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5600 | 48.3 | 49.1 | $-2961.02 |
| ETH | 6113 | 48.2 | 48.5 | $-3754.62 |
| SOL | 6409 | 48.2 | 48.5 | $-3655.55 |
| XRP | 6433 | 48.3 | 48.5 | $-3582.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

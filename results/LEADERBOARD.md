# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 4:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 752 windows, 20753 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 393 | 33.8 | 34.9 | $-281.45 | -7.2% | $718.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2121 | 51.5 | 50.5 | $-498.13 | -2.3% | $501.87 | -1.1 | done | can't tell from luck |
| value_ev10 | 952 | 37.9 | 39.1 | $-618.43 | -6.5% | $381.57 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1754 | 50.0 | 49.6 | $-656.23 | -3.7% | $343.77 | -1.6 | done | can't tell from luck |
| value_ev5 | 1435 | 40.3 | 41.1 | $-799.82 | -5.6% | $200.18 | -1.8 | done | can't tell from luck |
| trend_filter | 1223 | 49.8 | 50.9 | $-813.12 | -6.6% | $186.88 | -2.4 | done | losing for real |
| coinflip | 3000 | 50.4 | 50.2 | $-1114.02 | -3.7% | $-114.02 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1754 | 50.0 | 51.2 | $-1205.67 | -6.9% | $-205.67 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2121 | 48.5 | 50.2 | $-1540.50 | -7.3% | $-540.50 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3000 | 50.8 | 51.8 | $-1680.76 | -5.6% | $-680.76 | -3.2 | done | losing for real |
| always_up | 3000 | 46.9 | 49.6 | $-2852.32 | -9.5% | $-1852.32 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4702 | 48.1 | 49.1 | $-2893.72 |
| ETH | 5171 | 48.1 | 48.6 | $-3368.67 |
| SOL | 5405 | 48.0 | 48.6 | $-3223.28 |
| XRP | 5475 | 48.5 | 48.4 | $-2574.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 512 windows, 14120 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1200 | 51.0 | 49.8 | $-221.51 | -1.8% | $778.49 | -0.6 | done | can't tell from luck |
| value_ev10 | 661 | 38.1 | 39.7 | $-493.23 | -7.5% | $506.77 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1432 | 49.7 | 49.6 | $-564.62 | -3.9% | $435.38 | -1.5 | done | can't tell from luck |
| trend_filter | 830 | 49.3 | 50.8 | $-599.18 | -7.2% | $400.82 | -2.1 | done | losing for real |
| value_ev5 | 981 | 40.1 | 41.5 | $-689.96 | -7.0% | $310.04 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1432 | 50.3 | 51.6 | $-948.87 | -6.6% | $51.13 | -2.6 | done | losing for real |
| coinflip | 2040 | 50.0 | 50.7 | $-1063.82 | -5.2% | $-63.82 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1200 | 49.0 | 51.4 | $-1065.34 | -8.9% | $-65.34 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2040 | 49.5 | 51.6 | $-1607.95 | -7.9% | $-607.95 | -3.7 | done | losing for real |
| always_up | 2040 | 46.3 | 50.1 | $-2351.50 | -11.5% | $-1351.50 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3195 | 47.3 | 49.2 | $-2589.87 |
| ETH | 3528 | 48.0 | 48.7 | $-2313.29 |
| SOL | 3679 | 47.6 | 49.0 | $-2699.00 |
| XRP | 3718 | 48.3 | 48.8 | $-2182.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

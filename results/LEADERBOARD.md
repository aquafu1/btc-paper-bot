# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 12:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1171 windows, 32390 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 623 | 35.0 | 35.3 | $-341.04 | -5.5% | $658.96 | -1.0 | done | can't tell from luck |
| value_ev10 | 1531 | 38.5 | 39.2 | $-802.45 | -5.2% | $197.55 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3248 | 50.8 | 50.4 | $-1074.68 | -3.3% | $-74.68 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2734 | 49.7 | 49.4 | $-1173.71 | -4.3% | $-173.71 | -2.2 | done | losing for real |
| value_ev5 | 2318 | 40.3 | 41.1 | $-1248.93 | -5.4% | $-248.93 | -2.2 | done | losing for real |
| trend_filter | 1920 | 49.0 | 50.5 | $-1529.13 | -8.0% | $-529.13 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2734 | 50.3 | 51.1 | $-1698.51 | -6.2% | $-698.51 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3248 | 49.2 | 50.2 | $-1944.81 | -6.0% | $-944.81 | -3.4 | done | losing for real |
| coinflip | 4678 | 50.1 | 50.2 | $-2072.88 | -4.4% | $-1072.88 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4678 | 50.2 | 51.4 | $-2892.66 | -6.2% | $-1892.66 | -4.4 | done | losing for real |
| always_up | 4678 | 47.8 | 49.3 | $-3418.89 | -7.3% | $-2418.89 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7435 | 48.2 | 49.0 | $-3907.37 |
| ETH | 8040 | 48.1 | 48.4 | $-4761.07 |
| SOL | 8420 | 48.1 | 48.4 | $-4472.76 |
| XRP | 8495 | 48.1 | 48.2 | $-5056.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

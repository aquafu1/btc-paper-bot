# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 515 windows, 14196 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 265 | 34.3 | 35.5 | $-188.91 | -7.1% | $811.09 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1207 | 51.1 | 49.9 | $-211.13 | -1.7% | $788.88 | -0.6 | done | can't tell from luck |
| value_ev10 | 662 | 38.1 | 39.7 | $-503.23 | -7.6% | $496.77 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1441 | 49.7 | 49.6 | $-589.85 | -4.1% | $410.15 | -1.6 | done | can't tell from luck |
| trend_filter | 832 | 49.3 | 50.8 | $-603.24 | -7.3% | $396.76 | -2.1 | done | losing for real |
| value_ev5 | 985 | 39.9 | 41.5 | $-729.96 | -7.4% | $270.04 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1441 | 50.3 | 51.6 | $-955.58 | -6.6% | $44.42 | -2.6 | done | losing for real |
| coinflip | 2052 | 50.0 | 50.7 | $-1087.25 | -5.3% | $-87.25 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1207 | 48.9 | 51.3 | $-1101.69 | -9.1% | $-101.69 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2052 | 49.4 | 51.6 | $-1663.98 | -8.1% | $-663.98 | -3.8 | done | losing for real |
| always_up | 2052 | 46.4 | 50.1 | $-2341.10 | -11.4% | $-1341.10 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3214 | 47.3 | 49.2 | $-2613.45 |
| ETH | 3546 | 48.0 | 48.7 | $-2368.22 |
| SOL | 3698 | 47.6 | 49.0 | $-2790.01 |
| XRP | 3738 | 48.3 | 48.8 | $-2204.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 440 windows, 12111 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 220 | 34.5 | 36.1 | $-178.23 | -8.1% | $821.77 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1037 | 51.2 | 50.0 | $-186.95 | -1.8% | $813.05 | -0.6 | done | can't tell from luck |
| trend_filter | 701 | 50.4 | 50.6 | $-329.69 | -4.7% | $670.31 | -1.3 | done | can't tell from luck |
| value_ev10 | 569 | 38.7 | 40.2 | $-423.63 | -7.4% | $576.37 | -1.5 | done | can't tell from luck |
| value_ev5 | 847 | 41.0 | 41.9 | $-519.11 | -6.1% | $480.89 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1222 | 49.6 | 50.0 | $-544.64 | -4.5% | $455.36 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1222 | 50.4 | 51.7 | $-837.47 | -6.9% | $162.53 | -2.5 | done | losing for real |
| coinflip | 1752 | 50.3 | 50.9 | $-845.22 | -4.8% | $154.78 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1037 | 48.8 | 51.8 | $-1045.00 | -10.1% | $-45.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1752 | 49.8 | 51.6 | $-1215.03 | -6.9% | $-215.03 | -3.0 | done | losing for real |
| always_up | 1752 | 45.8 | 50.5 | $-2265.34 | -12.9% | $-1265.34 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2738 | 47.6 | 49.3 | $-2107.01 |
| ETH | 3039 | 48.0 | 48.8 | $-1940.78 |
| SOL | 3144 | 47.7 | 49.3 | $-2521.36 |
| XRP | 3190 | 48.6 | 49.3 | $-1821.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

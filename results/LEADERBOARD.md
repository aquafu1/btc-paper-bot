# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 278 windows, 7339 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 723 | 54.8 | 52.1 | $+94.35 | +1.3% | $1094.35 | +0.4 | done | can't tell from luck |
| value_ev20 | 135 | 36.3 | 36.9 | $-79.35 | -5.9% | $920.65 | -0.5 | Sun 5:15 AM | too few trades (135/200) |
| reversal_60m_0.30pct | 588 | 52.2 | 52.1 | $-211.43 | -3.6% | $788.57 | -0.9 | done | can't tell from luck |
| value_ev10 | 356 | 38.8 | 40.8 | $-303.02 | -8.5% | $696.98 | -1.4 | done | can't tell from luck |
| value_ev5 | 521 | 40.5 | 42.4 | $-436.88 | -8.4% | $563.12 | -1.7 | done | can't tell from luck |
| trend_filter | 390 | 46.7 | 50.3 | $-456.54 | -11.7% | $543.46 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 588 | 47.8 | 49.7 | $-500.58 | -8.5% | $499.42 | -2.1 | done | losing for real |
| coinflip | 1105 | 50.0 | 50.9 | $-654.50 | -5.9% | $345.50 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1105 | 49.6 | 51.5 | $-849.07 | -7.7% | $150.93 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 723 | 45.2 | 49.8 | $-936.07 | -12.9% | $63.93 | -3.5 | done | losing for real |
| always_up | 1105 | 46.9 | 50.2 | $-1170.23 | -10.6% | $-170.23 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1647 | 46.8 | 49.5 | $-1582.76 |
| ETH | 1833 | 47.1 | 48.9 | $-1646.08 |
| SOL | 1897 | 48.3 | 49.4 | $-1408.81 |
| XRP | 1962 | 48.9 | 49.1 | $-865.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

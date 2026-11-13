# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 278 windows, 7333 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 722 | 54.7 | 52.1 | $+86.11 | +1.2% | $1086.11 | +0.3 | done | can't tell from luck |
| value_ev20 | 135 | 36.3 | 36.9 | $-79.35 | -5.9% | $920.65 | -0.5 | Sun 5:00 AM | too few trades (135/200) |
| reversal_60m_0.30pct | 588 | 52.2 | 52.1 | $-211.43 | -3.6% | $788.57 | -0.9 | done | can't tell from luck |
| value_ev10 | 356 | 38.8 | 40.8 | $-303.02 | -8.5% | $696.98 | -1.4 | done | can't tell from luck |
| value_ev5 | 520 | 40.6 | 42.4 | $-426.88 | -8.2% | $573.12 | -1.6 | done | can't tell from luck |
| trend_filter | 390 | 46.7 | 50.3 | $-456.54 | -11.7% | $543.46 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 588 | 47.8 | 49.7 | $-500.58 | -8.5% | $499.42 | -2.1 | done | losing for real |
| coinflip | 1104 | 49.9 | 50.9 | $-662.75 | -6.0% | $337.25 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1104 | 49.6 | 51.5 | $-839.07 | -7.6% | $160.93 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 722 | 45.3 | 49.8 | $-926.07 | -12.8% | $73.93 | -3.5 | done | losing for real |
| always_up | 1104 | 46.8 | 50.2 | $-1178.48 | -10.7% | $-178.48 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1641 | 46.7 | 49.4 | $-1577.50 |
| ETH | 1833 | 47.1 | 48.9 | $-1646.08 |
| SOL | 1897 | 48.3 | 49.4 | $-1408.81 |
| XRP | 1962 | 48.9 | 49.1 | $-865.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 102 windows, 2607 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 196 | 58.2 | 52.9 | $+142.58 | +7.3% | $1142.58 | +1.1 | Wed 7:30 PM | too few trades (196/200) |
| reversal_15m_0.10pct | 252 | 56.0 | 52.1 | $+130.19 | +5.2% | $1130.19 | +0.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 400 | 53.5 | 50.8 | $+65.86 | +1.6% | $1065.86 | +0.3 | done | can't tell from luck |
| value_ev10 | 138 | 39.1 | 40.5 | $-109.31 | -7.9% | $890.69 | -0.8 | Thu 7:15 AM | too few trades (138/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 5:15 AM | too few trades (50/200) |
| trend_filter | 137 | 44.5 | 49.0 | $-168.60 | -12.3% | $831.40 | -1.4 | Thu 7:30 AM | too few trades (137/200) |
| coinflip | 400 | 50.5 | 51.4 | $-220.90 | -5.5% | $779.10 | -1.1 | done | can't tell from luck |
| value_ev5 | 186 | 37.1 | 41.8 | $-274.75 | -14.8% | $725.25 | -1.8 | Wed 9:00 PM | too few trades (186/200) |
| momentum_60m_0.30pct | 196 | 41.8 | 49.1 | $-341.39 | -17.4% | $658.61 | -2.4 | Wed 7:30 PM | too few trades (196/200) |
| always_up | 400 | 47.8 | 50.3 | $-345.37 | -8.6% | $654.63 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 252 | 44.0 | 49.9 | $-367.22 | -14.6% | $632.78 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 563 | 46.4 | 49.8 | $-419.81 |
| ETH | 637 | 46.3 | 48.9 | $-503.95 |
| SOL | 694 | 48.7 | 48.4 | $-409.04 |
| XRP | 713 | 50.4 | 49.0 | $-279.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.

# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 74 windows, 1838 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 288 | 56.6 | 51.0 | $+219.48 | +7.6% | $1219.48 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 128 | 61.7 | 52.5 | $+194.98 | +15.2% | $1194.98 | +1.8 | Wed 7:30 PM | too few trades (128/200) |
| reversal_15m_0.10pct | 173 | 56.6 | 51.9 | $+124.16 | +7.2% | $1124.16 | +1.0 | Wed 12:15 PM | too few trades (173/200) |
| value_ev10 | 98 | 43.9 | 39.5 | $+39.52 | +4.0% | $1039.52 | +0.3 | Thu 4:00 AM | too few trades (98/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 7:15 AM | too few trades (41/200) |
| value_ev5 | 137 | 41.6 | 41.1 | $-58.07 | -4.2% | $941.93 | -0.4 | Wed 5:45 PM | too few trades (137/200) |
| trend_filter | 96 | 44.8 | 48.7 | $-109.47 | -11.4% | $890.53 | -1.1 | Thu 4:45 AM | too few trades (96/200) |
| coinflip | 288 | 50.0 | 51.5 | $-178.45 | -6.2% | $821.55 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 173 | 43.4 | 49.5 | $-257.58 | -14.9% | $742.42 | -2.0 | Wed 12:15 PM | too few trades (173/200) |
| momentum_60m_0.30pct | 128 | 38.3 | 48.6 | $-297.99 | -23.3% | $702.01 | -2.6 | Wed 7:30 PM | too few trades (128/200) |
| always_up | 288 | 44.4 | 50.4 | $-427.22 | -14.8% | $572.78 | -2.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 387 | 47.5 | 49.9 | $-110.03 |
| ETH | 435 | 46.7 | 48.6 | $-234.87 |
| SOL | 504 | 49.2 | 48.1 | $-242.98 |
| XRP | 512 | 50.4 | 48.3 | $-196.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
